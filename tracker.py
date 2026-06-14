from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import datetime

import yfinance as yf


PERIOD_MAP = {
    "5d": {"period": "5d", "interval": "1h"},
    "1mo": {"period": "1mo", "interval": "1d"},
    "3mo": {"period": "3mo", "interval": "1d"},
    "6mo": {"period": "6mo", "interval": "1d"},
    "1y": {"period": "1y", "interval": "1d"},
    "2y": {"period": "2y", "interval": "1wk"},
    "5y": {"period": "5y", "interval": "1mo"},
}

HISTORY_FALLBACKS = {
    "1y": [
        {"period": "12mo", "interval": "1d"},
        {"period": "1y", "interval": "1wk"},
    ],
}

YIELD_SYMBOLS = {
    "^IRX",
    "^FVX",
    "^TNX",
    "^TYX",
}

BOND_ETF_SYMBOLS = {
    "SHY",
    "IEI",
    "IEF",
    "TLT",
    "UTWY",
    "GOVT",
    "TIP",
    "BND",
    "AGG",
    "LQD",
    "HYG",
}

BOND_NAME_KEYWORDS = (
    "treasury",
    "bond",
    "aggregate",
    "fixed income",
    "tips",
    "corporate bond",
    "high yield",
    "municipal",
    "債券",
    "公債",
)


@dataclass
class Quote:
    symbol: str
    name: str
    currency: str
    price: float
    previous_close: float
    change: float
    change_percent: float
    day_high: float | None
    day_low: float | None
    volume: int | None
    market_cap: int | None
    fifty_two_week_high: float | None
    fifty_two_week_low: float | None
    updated_at: str
    instrument_type: str = "stock"
    price_label: str = "現價"
    unit: str = ""


def normalize_symbol(symbol: str) -> str:
    return symbol.strip().upper()


def detect_instrument_type(info: dict, symbol: str) -> tuple[str, str, str]:
    if symbol in YIELD_SYMBOLS:
        return "yield", "殖利率", "%"

    if symbol in BOND_ETF_SYMBOLS:
        return "bond_etf", "淨值", "USD"

    quote_type = (info.get("quoteType") or "").upper()
    name = (info.get("shortName") or info.get("longName") or "").lower()

    if quote_type in {"ETF", "MUTUALFUND"} and any(keyword in name for keyword in BOND_NAME_KEYWORDS):
        return "bond_etf", "淨值", info.get("currency") or "USD"

    if quote_type == "INDEX" and any(keyword in name for keyword in ("treasury", "yield", "t-note", "t-bill")):
        return "yield", "殖利率", "%"

    return "stock", "現價", info.get("currency") or ""


def _price_digits(instrument_type: str) -> int:
    return 3 if instrument_type == "yield" else 4


def _quote_from_ticker(ticker: yf.Ticker, normalized: str) -> Quote:
    info = ticker.info

    price = info.get("currentPrice") or info.get("regularMarketPrice")
    previous_close = info.get("regularMarketPreviousClose") or info.get("previousClose")

    if price is None or previous_close is None:
        history = ticker.history(period="5d")
        if history.empty:
            raise ValueError(f"找不到股票代號：{normalized}")

        price = float(history["Close"].iloc[-1])
        previous_close = float(history["Close"].iloc[-2]) if len(history) > 1 else price

    change = float(price) - float(previous_close)
    change_percent = (change / float(previous_close) * 100) if previous_close else 0.0
    instrument_type, price_label, unit = detect_instrument_type(info, normalized)
    digits = _price_digits(instrument_type)

    return Quote(
        symbol=normalized,
        name=info.get("shortName") or info.get("longName") or normalized,
        currency=info.get("currency") or "",
        price=round(float(price), digits),
        previous_close=round(float(previous_close), digits),
        change=round(change, digits),
        change_percent=round(change_percent, 2),
        day_high=_optional_float(info.get("dayHigh") or info.get("regularMarketDayHigh"), digits),
        day_low=_optional_float(info.get("dayLow") or info.get("regularMarketDayLow"), digits),
        volume=_optional_int(info.get("volume") or info.get("regularMarketVolume")),
        market_cap=_optional_int(info.get("marketCap")),
        fifty_two_week_high=_optional_float(info.get("fiftyTwoWeekHigh"), digits),
        fifty_two_week_low=_optional_float(info.get("fiftyTwoWeekLow"), digits),
        updated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        instrument_type=instrument_type,
        price_label=price_label,
        unit=unit,
    )


def fetch_quote(symbol: str) -> Quote:
    normalized = normalize_symbol(symbol)
    return _quote_from_ticker(yf.Ticker(normalized), normalized)


def fetch_quotes(symbols: list[str]) -> dict:
    normalized_symbols = [normalize_symbol(symbol) for symbol in symbols if symbol.strip()]
    unique_symbols = list(dict.fromkeys(normalized_symbols))

    quotes: list[dict] = []
    errors: list[dict] = []

    for symbol in unique_symbols:
        try:
            quotes.append(quote_to_dict(fetch_quote(symbol)))
        except Exception as exc:
            errors.append({"symbol": symbol, "error": str(exc)})

    return {"quotes": quotes, "errors": errors}


def fetch_history(symbol: str, period_key: str = "1mo") -> dict:
    normalized = normalize_symbol(symbol)
    config = PERIOD_MAP.get(period_key, PERIOD_MAP["1mo"])
    configs_to_try = [config, *HISTORY_FALLBACKS.get(period_key, [])]

    ticker = yf.Ticker(normalized)
    history = None
    used_interval = config["interval"]

    for attempt in configs_to_try:
        attempt_history = ticker.history(period=attempt["period"], interval=attempt["interval"])
        if not attempt_history.empty:
            history = attempt_history
            used_interval = attempt["interval"]
            break

    if history is None or history.empty:
        raise ValueError(f"無法取得 {normalized} 的歷史資料")

    history = history.copy()
    history["Close"] = history["Close"].ffill().bfill()

    labels: list[str] = []
    prices: list[float] = []

    for index, row in history.iterrows():
        close = _finite_float(row["Close"])
        if close is None:
            continue

        if used_interval in {"1h", "1d"}:
            labels.append(index.strftime("%Y-%m-%d %H:%M"))
        elif used_interval == "1wk":
            labels.append(index.strftime("%Y-%m-%d"))
        else:
            labels.append(index.strftime("%Y-%m"))

        prices.append(close)

    if not prices:
        raise ValueError(f"無法取得 {normalized} 的有效歷史資料")

    start_price = prices[0]
    end_price = prices[-1]
    trend_change = end_price - start_price
    trend_percent = (trend_change / start_price * 100) if start_price else 0.0

    return {
        "symbol": normalized,
        "period": period_key,
        "labels": labels,
        "prices": prices,
        "start_price": start_price,
        "end_price": end_price,
        "trend_change": round(trend_change, 4),
        "trend_percent": round(trend_percent, 2),
    }


def fetch_histories(symbols: list[str], period_key: str = "1mo") -> dict:
    normalized_symbols = [normalize_symbol(symbol) for symbol in symbols if symbol.strip()]
    unique_symbols = list(dict.fromkeys(normalized_symbols))

    histories: list[dict] = []
    errors: list[dict] = []

    for symbol in unique_symbols:
        try:
            histories.append(fetch_history(symbol, period_key))
        except Exception as exc:
            errors.append({"symbol": symbol, "error": str(exc)})

    return {"histories": histories, "errors": errors}


def quote_to_dict(quote: Quote) -> dict:
    return {
        "symbol": quote.symbol,
        "name": quote.name,
        "currency": quote.currency,
        "price": quote.price,
        "previous_close": quote.previous_close,
        "change": quote.change,
        "change_percent": quote.change_percent,
        "day_high": quote.day_high,
        "day_low": quote.day_low,
        "volume": quote.volume,
        "market_cap": quote.market_cap,
        "fifty_two_week_high": quote.fifty_two_week_high,
        "fifty_two_week_low": quote.fifty_two_week_low,
        "updated_at": quote.updated_at,
        "instrument_type": quote.instrument_type,
        "price_label": quote.price_label,
        "unit": quote.unit,
    }


def _finite_float(value: object, digits: int = 4) -> float | None:
    if value is None:
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(number):
        return None
    return round(number, digits)


def _optional_float(value: object, digits: int = 4) -> float | None:
    return _finite_float(value, digits)


def _optional_int(value: object) -> int | None:
    if value is None:
        return None
    return int(value)

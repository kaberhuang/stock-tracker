from __future__ import annotations

import math
import time
from dataclasses import dataclass
from datetime import datetime
from threading import Lock

import pandas as pd
import yfinance as yf

try:
    from curl_cffi import requests as curl_requests
except ImportError:
    curl_requests = None


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

CACHE_TTL_SECONDS = 90
MAX_YAHOO_RETRIES = 3

_cache_lock = Lock()
_quote_cache: dict[str, tuple[float, dict]] = {}
_history_cache: dict[str, tuple[float, dict]] = {}
_yf_session: object | None = None


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


def get_yf_session() -> object | None:
    global _yf_session
    if _yf_session is not None:
        return _yf_session
    if curl_requests is not None:
        _yf_session = curl_requests.Session(impersonate="chrome")
    return _yf_session


def make_ticker(symbol: str) -> yf.Ticker:
    session = get_yf_session()
    if session is not None:
        return yf.Ticker(symbol, session=session)
    return yf.Ticker(symbol)


def _is_rate_limit_error(exc: Exception) -> bool:
    message = str(exc).lower()
    return "too many requests" in message or "rate limit" in message


def _call_yahoo_with_retry(action):
    delay = 1.0
    last_error: Exception | None = None

    for _ in range(MAX_YAHOO_RETRIES):
        try:
            return action()
        except Exception as exc:
            last_error = exc
            if _is_rate_limit_error(exc):
                time.sleep(delay)
                delay *= 2
                continue
            raise

    if last_error is not None:
        raise last_error
    raise RuntimeError("Yahoo Finance 請求失敗")


def _cache_get(cache: dict[str, tuple[float, dict]], key: str) -> dict | None:
    with _cache_lock:
        item = cache.get(key)
        if item and time.time() - item[0] < CACHE_TTL_SECONDS:
            return item[1]
    return None


def _cache_set(cache: dict[str, tuple[float, dict]], key: str, value: dict) -> None:
    with _cache_lock:
        cache[key] = (time.time(), value)


def _safe_history(ticker: yf.Ticker, **kwargs) -> pd.DataFrame:
    def fetch() -> pd.DataFrame:
        frame = ticker.history(**kwargs)
        if frame is None:
            return pd.DataFrame()
        return frame

    return _call_yahoo_with_retry(fetch)


def _safe_download(symbols: list[str], **kwargs) -> pd.DataFrame:
    session = get_yf_session()

    def fetch() -> pd.DataFrame:
        return yf.download(
            tickers=" ".join(symbols),
            progress=False,
            threads=False,
            session=session,
            **kwargs,
        )

    return _call_yahoo_with_retry(fetch)


def _safe_info(ticker: yf.Ticker) -> dict:
    def fetch() -> dict:
        info = ticker.info
        return info if isinstance(info, dict) else {}

    try:
        return _call_yahoo_with_retry(fetch)
    except Exception:
        return {}


def _safe_fast_info(ticker: yf.Ticker) -> dict:
    def fetch() -> dict:
        fast_info = ticker.fast_info
        if hasattr(fast_info, "items"):
            return dict(fast_info.items())
        return {}

    try:
        return _call_yahoo_with_retry(fetch)
    except Exception:
        return {}


def _close_prices_from_history(history: pd.DataFrame) -> tuple[float, float]:
    closes = history["Close"].ffill().bfill().dropna()
    if closes.empty:
        raise ValueError("無有效收盤價")
    price = float(closes.iloc[-1])
    previous_close = float(closes.iloc[-2]) if len(closes) > 1 else price
    return price, previous_close


def _extract_close_pair_from_download(data: pd.DataFrame, symbol: str) -> tuple[float, float] | None:
    if data.empty:
        return None

    if isinstance(data.columns, pd.MultiIndex):
        if symbol not in data.columns.get_level_values(0):
            return None
        closes = data[symbol]["Close"].ffill().bfill().dropna()
    else:
        if "Close" not in data.columns:
            return None
        closes = data["Close"].ffill().bfill().dropna()

    if closes.empty:
        return None

    price = float(closes.iloc[-1])
    previous_close = float(closes.iloc[-2]) if len(closes) > 1 else price
    return price, previous_close


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
    fast_info = _safe_fast_info(ticker)
    info = _safe_info(ticker)

    price = fast_info.get("last_price") or fast_info.get("regular_market_price")
    previous_close = fast_info.get("previous_close")
    currency = fast_info.get("currency") or info.get("currency") or ""

    if price is None or previous_close is None:
        history = _safe_history(ticker, period="5d")
        if history.empty:
            raise ValueError(f"找不到股票代號：{normalized}")
        price, previous_close = _close_prices_from_history(history)

    change = float(price) - float(previous_close)
    change_percent = (change / float(previous_close) * 100) if previous_close else 0.0
    instrument_type, price_label, unit = detect_instrument_type(info, normalized)
    digits = _price_digits(instrument_type)

    return Quote(
        symbol=normalized,
        name=info.get("shortName") or info.get("longName") or normalized,
        currency=currency,
        price=round(float(price), digits),
        previous_close=round(float(previous_close), digits),
        change=round(change, digits),
        change_percent=round(change_percent, 2),
        day_high=_optional_float(
            fast_info.get("day_high")
            or fast_info.get("regular_market_day_high")
            or info.get("dayHigh")
            or info.get("regularMarketDayHigh"),
            digits,
        ),
        day_low=_optional_float(
            fast_info.get("day_low")
            or fast_info.get("regular_market_day_low")
            or info.get("dayLow")
            or info.get("regularMarketDayLow"),
            digits,
        ),
        volume=_optional_int(
            fast_info.get("last_volume")
            or fast_info.get("ten_day_average_volume")
            or info.get("volume")
            or info.get("regularMarketVolume")
        ),
        market_cap=_optional_int(info.get("marketCap")),
        fifty_two_week_high=_optional_float(
            fast_info.get("year_high") or info.get("fiftyTwoWeekHigh"),
            digits,
        ),
        fifty_two_week_low=_optional_float(
            fast_info.get("year_low") or info.get("fiftyTwoWeekLow"),
            digits,
        ),
        updated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        instrument_type=instrument_type,
        price_label=price_label,
        unit=unit,
    )


def fetch_quote(symbol: str) -> Quote:
    normalized = normalize_symbol(symbol)
    cached = _cache_get(_quote_cache, normalized)
    if cached is not None:
        return Quote(**cached)

    quote = _quote_from_ticker(make_ticker(normalized), normalized)
    _cache_set(_quote_cache, normalized, quote.__dict__.copy())
    return quote


def _build_quote_dict(symbol: str, close_pair: tuple[float, float] | None = None) -> dict:
    ticker = make_ticker(symbol)
    if close_pair is None:
        return quote_to_dict(_quote_from_ticker(ticker, symbol))

    fast_info = _safe_fast_info(ticker)
    info: dict = {}
    if symbol not in YIELD_SYMBOLS and symbol not in BOND_ETF_SYMBOLS:
        info = _safe_info(ticker)

    price, previous_close = close_pair
    change = price - previous_close
    change_percent = (change / previous_close * 100) if previous_close else 0.0
    instrument_type, price_label, unit = detect_instrument_type(info, symbol)
    digits = _price_digits(instrument_type)

    quote = Quote(
        symbol=symbol,
        name=info.get("shortName") or info.get("longName") or symbol,
        currency=fast_info.get("currency") or info.get("currency") or "",
        price=round(price, digits),
        previous_close=round(previous_close, digits),
        change=round(change, digits),
        change_percent=round(change_percent, 2),
        day_high=_optional_float(
            fast_info.get("day_high") or info.get("dayHigh") or info.get("regularMarketDayHigh"),
            digits,
        ),
        day_low=_optional_float(
            fast_info.get("day_low") or info.get("dayLow") or info.get("regularMarketDayLow"),
            digits,
        ),
        volume=_optional_int(
            fast_info.get("last_volume")
            or fast_info.get("ten_day_average_volume")
            or info.get("volume")
            or info.get("regularMarketVolume")
        ),
        market_cap=_optional_int(info.get("marketCap")),
        fifty_two_week_high=_optional_float(
            fast_info.get("year_high") or info.get("fiftyTwoWeekHigh"),
            digits,
        ),
        fifty_two_week_low=_optional_float(
            fast_info.get("year_low") or info.get("fiftyTwoWeekLow"),
            digits,
        ),
        updated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        instrument_type=instrument_type,
        price_label=price_label,
        unit=unit,
    )
    return quote_to_dict(quote)


def fetch_quotes(symbols: list[str]) -> dict:
    normalized_symbols = [normalize_symbol(symbol) for symbol in symbols if symbol.strip()]
    unique_symbols = list(dict.fromkeys(normalized_symbols))

    quotes: list[dict] = []
    errors: list[dict] = []
    pending_symbols: list[str] = []

    for symbol in unique_symbols:
        cached = _cache_get(_quote_cache, symbol)
        if cached is not None:
            quotes.append(cached)
        else:
            pending_symbols.append(symbol)

    batch_prices: dict[str, tuple[float, float]] = {}
    if pending_symbols:
        try:
            download_data = _safe_download(
                pending_symbols,
                period="5d",
                interval="1d",
                group_by="ticker",
            )
            for symbol in pending_symbols:
                close_pair = _extract_close_pair_from_download(download_data, symbol)
                if close_pair is not None:
                    batch_prices[symbol] = close_pair
        except Exception:
            batch_prices = {}

        for index, symbol in enumerate(pending_symbols):
            try:
                if index > 0:
                    time.sleep(0.35)
                quote_dict = _build_quote_dict(symbol, batch_prices.get(symbol))
                _cache_set(_quote_cache, symbol, quote_dict)
                quotes.append(quote_dict)
            except Exception as exc:
                errors.append({"symbol": symbol, "error": str(exc)})

    return {"quotes": quotes, "errors": errors}


def fetch_history(symbol: str, period_key: str = "1mo") -> dict:
    normalized = normalize_symbol(symbol)
    cache_key = f"{normalized}:{period_key}"
    cached = _cache_get(_history_cache, cache_key)
    if cached is not None:
        return cached

    config = PERIOD_MAP.get(period_key, PERIOD_MAP["1mo"])
    configs_to_try = [config, *HISTORY_FALLBACKS.get(period_key, [])]

    ticker = make_ticker(normalized)
    history = None
    used_interval = config["interval"]

    for attempt in configs_to_try:
        attempt_history = _safe_history(
            ticker,
            period=attempt["period"],
            interval=attempt["interval"],
        )
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

    payload = {
        "symbol": normalized,
        "period": period_key,
        "labels": labels,
        "prices": prices,
        "start_price": start_price,
        "end_price": end_price,
        "trend_change": round(trend_change, 4),
        "trend_percent": round(trend_percent, 2),
    }
    _cache_set(_history_cache, cache_key, payload)
    return payload


def fetch_histories(symbols: list[str], period_key: str = "1mo") -> dict:
    normalized_symbols = [normalize_symbol(symbol) for symbol in symbols if symbol.strip()]
    unique_symbols = list(dict.fromkeys(normalized_symbols))

    histories: list[dict] = []
    errors: list[dict] = []

    for index, symbol in enumerate(unique_symbols):
        try:
            if index > 0:
                time.sleep(0.25)
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
    try:
        return int(value)
    except (TypeError, ValueError):
        return None

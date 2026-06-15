from __future__ import annotations

import argparse
import math
import os
import socket
import threading
import webbrowser
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory

from tracker import fetch_histories, fetch_history, fetch_quote, fetch_quotes, quote_to_dict

try:
    from curl_cffi import requests as curl_requests
except ImportError:
    curl_requests = None

BASE_DIR = Path(__file__).resolve().parent
WEB_DIR = BASE_DIR / "web"
DEFAULT_PORT = 8768

app = Flask(__name__, static_folder=str(WEB_DIR), static_url_path="")


def sanitize_json(value: object) -> object:
    if isinstance(value, dict):
        return {key: sanitize_json(item) for key, item in value.items()}
    if isinstance(value, list):
        return [sanitize_json(item) for item in value]
    if isinstance(value, float) and not math.isfinite(value):
        return None
    return value


def json_response(payload: object, status: int = 200) -> object:
    return jsonify(sanitize_json(payload)), status


@app.get("/")
def index() -> object:
    index_path = WEB_DIR / "index.html"
    if not index_path.exists():
        return json_response(
            {
                "error": "找不到 web/index.html，請確認 GitHub 有上傳 web 資料夾",
                "web_dir": str(WEB_DIR),
            },
            500,
        )
    return send_from_directory(WEB_DIR, "index.html")


@app.get("/health")
def health() -> object:
    index_path = WEB_DIR / "index.html"
    return json_response(
        {
            "status": "ok",
            "web_dir_exists": WEB_DIR.exists(),
            "index_exists": index_path.exists(),
            "curl_cffi_enabled": curl_requests is not None,
        }
    )


@app.get("/api/quote/<symbol>")
def get_quote(symbol: str) -> object:
    try:
        quote = fetch_quote(symbol)
        return json_response(quote_to_dict(quote))
    except Exception as exc:
        return json_response({"error": str(exc)}, 400)


@app.post("/api/quotes")
def get_quotes() -> object:
    payload = request.get_json(silent=True) or {}
    symbols = payload.get("symbols", [])

    if not isinstance(symbols, list) or not symbols:
        return json_response({"error": "請提供至少一個股票代號"}, 400)

    return json_response(fetch_quotes(symbols))


@app.post("/api/histories")
def get_histories() -> object:
    payload = request.get_json(silent=True) or {}
    symbols = payload.get("symbols", [])
    period = payload.get("period", "1mo")

    if not isinstance(symbols, list) or not symbols:
        return json_response({"error": "請提供至少一個股票代號"}, 400)

    return json_response(fetch_histories(symbols, period))


@app.get("/api/history/<symbol>")
def get_history(symbol: str) -> object:
    period = request.args.get("period", "1mo")
    try:
        return json_response(fetch_history(symbol, period))
    except Exception as exc:
        return json_response({"error": str(exc)}, 400)


def local_ip() -> str | None:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect(("8.8.8.8", 80))
            return sock.getsockname()[0]
    except OSError:
        return None


def main() -> None:
    parser = argparse.ArgumentParser(description="股價趨勢追蹤網頁伺服器")
    parser.add_argument(
        "--share",
        action="store_true",
        help="允許同一區域網路內的其他裝置連線",
    )
    args = parser.parse_args()

    port = int(os.environ.get("PORT", DEFAULT_PORT))
    host = "0.0.0.0" if args.share else "127.0.0.1"
    local_url = f"http://127.0.0.1:{port}"

    print(f"股價趨勢追蹤：{local_url}")
    if args.share:
        ip = local_ip()
        if ip:
            print(f"區域網路分享：http://{ip}:{port}")
            print("同一 WiFi 或區域網路內的裝置，可用上方網址開啟")
        else:
            print("無法偵測本機 IP，請在終端機執行 ipconfig 查看 IPv4 位址")
        print("若 Windows 防火牆詢問，請允許 Python 存取私人網路")
    else:
        print("僅本機可連線。若要分享給同網路的人，請加上 --share 參數")
    print("按 Ctrl+C 可停止伺服器")

    threading.Timer(1.0, lambda: webbrowser.open(local_url)).start()
    app.run(host=host, port=port, debug=False, use_reloader=False)


if __name__ == "__main__":
    main()

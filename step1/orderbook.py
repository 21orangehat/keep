from httpx import get

from utils import BINANCE_FUTURES_REST_API, analyze_data


def get_data(symbol: str = "BTCUSDT", limit: int = 50) -> list:
    URL: str = f"{BINANCE_FUTURES_REST_API}/depth?symbol={symbol}&limit={limit}"

    data: dict = get(URL).json()

    return data


def main() -> None:
    data = get_data()
    print(data)
    analyze_data(data)


if __name__ == '__main__':
    main()

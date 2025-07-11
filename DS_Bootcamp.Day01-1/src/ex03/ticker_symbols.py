import sys


def ticker():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    if len(sys.argv) == 2:
        ticker = sys.argv[1]
        if ticker.upper() not in STOCKS:
            print("Unknown ticker")
        else:
            result = []
            for key, value in COMPANIES.items():
                if value == ticker.upper():
                    result.append(key)
            result.append(STOCKS[ticker.upper()])
            print(*result, sep=', ')
    else:
        sys.exit(0)


if __name__ == '__main__':
    ticker()

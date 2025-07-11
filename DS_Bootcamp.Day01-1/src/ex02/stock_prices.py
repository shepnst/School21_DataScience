
import sys


def price():
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
        if sys.argv[1].capitalize() not in COMPANIES:
            print("Unknown company")
        else:
            print(STOCKS[COMPANIES[sys.argv[1].capitalize()]])
    else:
        sys.exit(0)


if __name__ == '__main__':
    price()

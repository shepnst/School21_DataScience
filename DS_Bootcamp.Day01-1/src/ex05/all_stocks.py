import sys


def stocks():
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
    arg = sys.argv
    if len(arg) == 2:
        temp = arg[1].replace(" ", "").split(',')
        for i in temp:
            if i == '':
                sys.exit(0)
        for i in temp:
            if i.upper() in STOCKS:
                for key, value in COMPANIES.items():
                    if value == i.upper():
                        print(f'{i} is a ticker symbol for {key}')
            elif i.capitalize() in COMPANIES:
                print(
                    f'{i} stock price is {STOCKS[COMPANIES[i.capitalize()]]}')
            elif i.capitalize() not in COMPANIES or i.upper() not in STOCKS:
                print(f'{i} is an unknown company or an unknown ticker symbol')
    else:
        sys.exit(0)


if __name__ == '__main__':
    stocks()

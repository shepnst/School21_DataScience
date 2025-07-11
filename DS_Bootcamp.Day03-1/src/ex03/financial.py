from bs4 import BeautifulSoup
import requests
import sys
import time

def parsing(ticker, field):
    url = f'https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}'
    time.sleep(5)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('div', class_='tableBody')
        if table is None:
            raise Exception('no data found for the ticker')
        rows = table.find_all('div', class_='row')
        flag_field = False
        for row in rows:
            col = row.find_all('div', class_='column')
            if col and col[0].text.strip() == field:
                res = [c.text.strip().replace('.00', '') for c in col]
                flag_field = True
                return tuple(res)
        if flag_field == False:
            raise Exception('the field wasn`t found')
    else:
        raise Exception('couldn`t connect to the website')


if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            print(parsing(sys.argv[1], sys.argv[2]))
        except Exception as error:
            print(error)
    else:
        raise ValueError('wrong number of arguments/usage')

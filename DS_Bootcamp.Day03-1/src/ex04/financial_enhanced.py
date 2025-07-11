from bs4 import BeautifulSoup
import httpx
import sys
import time
import pstats
import profile
def parsing(ticker, field):
    url = f'https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}'
    #time.sleep(5)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = httpx.get(url, headers=headers, follow_redirects=True)


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
            #print(parsing(sys.argv[1], sys.argv[2]))
            p=profile.Profile()
            p.run("parsing(sys.argv[1], sys.argv[2])")
            stat=pstats.Stats(p)
            stat.sort_stats("cumtime").print_stats(5)
        except Exception as error:
            print(error)
    else:
        raise ValueError('wrong number of arguments/usage')




#to run:
# python3 -m cProfile -s time financial_enhanced.py 'MSFT' 'Total Revenue' > profiling-http.txt
# python3 -m cProfile -s ncalls financial_enhanced.py 'MSFT' 'Total Revenue' > profiling-ncalls.txt
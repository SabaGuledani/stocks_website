import sqlite3
import requests
import json
from datetime import date
from datetime import timedelta

today = date.today()
date = today - timedelta(days = 1)

ticker = "AAPL"
apikey = 'WI1GOdsaBMaVnImCyZqgHc__H70kDtJ5'
url = f'https://api.polygon.io/v1/open-close/{ticker}/{date}?adjusted=true&apiKey={apikey}'

url2 = f'https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={apikey}'

r = requests.get(url)
r2 = requests.get(url2)
print(r)
print(r.headers)

result_json = r.text
res = json.loads(result_json)
#
res2 = json.loads(r2.text)

res_structured = json.dumps(res, indent=4)
res_structured2 = json.dumps(res2, indent=4)
print(res_structured)
print(res_structured2)

with open(f'{ticker}.json', 'w') as file:
    file.write(result_json)
    json.dump(res, file, indent=4)

date = res['from']
high = res['high']
low = res['low']
avg = (high+low)/2

#
previous_close = res["close"]
industry = res2["results"]['sic_description']
print(industry)
stock_open = res['open']
d_range = high-low
volume = res['volume']
after_hours = res['afterHours']

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


r = requests.get(url)

print(r)
print(r.headers)

result_json = r.text
res = json.loads(result_json)
res_structured = json.dumps(res, indent=4)
print(res_structured)

with open(f'{ticker}.json', 'w') as file:
    file.write(result_json)
    json.dump(res, file, indent=4)

date = res['from']
high = res['high']
low = res['low']
avg = (high+low)/2



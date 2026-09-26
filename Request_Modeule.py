import requests as req
import pandas as pd

res = req.get('https://api.restful-api.dev/objects')
if res.status_code == 200:
    print('Request Successful')

data = res.json()
print(data)

for obj in data:
    print(obj['id'])
    if obj['id'] == '1':
        print(obj['id']['capacity'])

df = pd.json_normalize(res.json())
print(df)

print('--------------------------------------------')
prod_ids = [('id',7),('id',5)]

res = req.get('https://api.restful-api.dev/objects', params=prod_ids)
if res.status_code == 200:
    print('Request Successful')

data = res.json()
print(data)

print('--------------------------------------------')
prod_ids = 7

res = req.get(f'https://api.restful-api.dev/objects/{prod_ids}')
if res.status_code == 200:
    print('Request Successful')

data = res.json()
print(data)


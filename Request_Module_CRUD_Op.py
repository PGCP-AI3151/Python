import requests as req

payload = {
  "name": "Apple MacBook Pro 16",
  "data": {
    "year": 2019,
    "price": 1849.99,
    "CPU model": "Intel Core i9",
    "Hard disk size": "1 TB"
  }
}

headers = {
    "Content-Type": "application/json",
}

res = req.post('https://api.restful-api.dev/objects', json=payload, headers=headers)

print(res.status_code)
res_data = res.json()
print(res_data)

prod_id = res_data['id']

res = req.put(f'https://api.restful-api.dev/objects/{prod_id}', json=payload, headers=headers)
print(res.status_code)
res_data = res.json()
print(res_data)

res = req.delete(f'https://api.restful-api.dev/objects/{prod_id}')
print(res.status_code)
res_data = res.json()
print(res_data)
import requests

res = requests.request('get', 'https://shoeisha.jp/')
print(res.status_code)
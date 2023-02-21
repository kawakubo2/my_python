import requests, os

url = 'https://uta.pw/shodou/img/3/3.png'

res = requests.get(url)

if not res.ok:
    print("失敗:", res.status_code)
    quit()

file = os.path.join(os.path.dirname(__file__), 'gyudon.png')


with open(file, 'wb') as fp:
    fp.write(res.content)

print("ok.")
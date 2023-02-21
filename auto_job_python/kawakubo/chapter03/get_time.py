import requests

# 現在時刻を提供しているサーバにアクセス
url = 'https://api.aoikujira.com/time/get.php'
result = requests.get(url)
print(result.text)
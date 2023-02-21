import requests

# url = 'https://api.aoikujira.com/time/get.php'
url = 'https://haru-idea.jp'
result = requests.get(url)
print(result.text)
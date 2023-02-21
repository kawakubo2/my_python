import requests

url = 'https://api.aoikujira.com/time/get.php'
# url = 'https://haru-idea.jp/courses'

result = requests.get(url)
print("ok=", result.ok)
if result.ok:
    print("text=", result.text)
    print("status_code=", result.status_code)
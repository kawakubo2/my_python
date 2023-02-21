import requests
res = requests.get('https://wings.msn.to/tmp/post.php?name=Yamada')
# params={'name': '佐々木新之助'})



print(res.text)
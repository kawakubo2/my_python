import os, requests

# 画像ファイルのURL
# url = "https://haru-idea.jp/images/haru0007_md.jpg"
url = "https://uta.pw/shodou/img/3/3.png"

# URLのリソースを取得
res = requests.get(url)

# 戻り値をチェック
if not res.ok:
    print("失敗:", res.status_code)
    quit()

# ファイルに保存
# with open(os.path.dirname(__file__) + "/robot1.png", "wb") as fp:
with open(os.path.dirname(__file__) + "/gyudon.png", "wb") as fp:
    fp.write(res.content)

print('ok')

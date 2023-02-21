import re # re --- Regular Expression 正規表現

pattern = re.compile(r"^[0-9]{3}-[0-9]{4}$")

while True:
    s = input('郵便番号(終了時はq): ')
    if s == 'q': break
    result = pattern.search(s)
    if result:
        print('○')
    else:
        print('×')
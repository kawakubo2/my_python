import re # re --- Regular Expression 正規表現

while True:
    s = input('正規表現(終了時はq): ')
    if s == 'q':
        break
    pattern = re.compile(s)

    """
    \はエスケープシーケンスを表す文字です
    """
    while True:
        s = input('対象文字列(次の正規表現の場合n): ')
        if s == 'n': break
        result = pattern.search(s)
        if result:
            print('○')
        else:
            print('×')
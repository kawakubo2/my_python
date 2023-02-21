s = "私の実家は〒812-0013です。"

pos = s.find("〒")

if pos != -1:
    print('郵便番号は' + s[pos+1:pos+9])
else:
    print('郵便番号が見つかりません')


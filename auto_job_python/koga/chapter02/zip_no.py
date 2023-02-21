s = '私の会社は〒123-4567です。'

if '〒' in s:
    print('郵便番号が含まれています。')
else:
    print('郵便番号が含まれていません')

pos = s.find('〒')
if pos > -1:
    print("郵便番号: {}".format(s[pos+1:pos+9]))
else:
    print("郵便番号は含まれていません。")
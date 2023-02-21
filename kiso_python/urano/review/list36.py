list36 = ['山田', '山口', '佐藤', '田中', '田口', '田代', '山本', '太田']

keywd = '田'

#
# 名前の中にkeywdを含む人を表示
# 山田 田中 田口 田代 太田
#
for name in list36:
    if keywd in name:
        print(name)
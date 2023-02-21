# -*- coding: utf-8 -*-

# =============================================================================
# str1 = "水金地火木土"
# 
# str2 = input("検索文字列 : ")
# 
# 
# try:
#     index = str1.index(str2)
#     print('"' + str2 + '"がみつかりました')
#     print("インデックス:", index)
# except ValueError:
#     print('"' + str2 + '"が見つかりませんでした')
# =============================================================================

email = 'tomo.kawakubo@gmail.com'

pos = email.index('@')

user = email[:pos]
domain = email[pos + len('@'):]

print('ユーザ部:', user, ' ドメイン部:', domain)
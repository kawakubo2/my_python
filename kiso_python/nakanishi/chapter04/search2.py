str1 = "水金地火木土"

str2 = input("検索文字列を入力してください: ")

index = str1.find(str2)

if index != -1:
    print('"' + str2 + '"が見つかりました')
    print(f"インデックス: {index}")
else:
    print('"' + str2 + '"が見つかりませんでした')
    print(f"インデックス: {index}")
    
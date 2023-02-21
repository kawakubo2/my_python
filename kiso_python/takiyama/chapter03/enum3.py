countries = ["フランス", "アメリカ", "中国", "ドイツ", "日本"]

for index, country in enumerate(countries):
    if index % 2 == 0:
        print('xxx')
    else:
        print('yyy')
    print(f"{index+1}: {country}")
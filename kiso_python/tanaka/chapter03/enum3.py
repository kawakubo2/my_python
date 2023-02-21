countries = ['フランス', 'アメリカ', '中国', 'ドイツ', '日本', 'イタリア']

for i, country in enumerate(countries):
    if i == 0:
        print(f"優勝: {country}")
    elif i == len(countries) - 1:
        print(f"ビリ: {country}")
    else:
        print(f" {i+1}位: {country}")
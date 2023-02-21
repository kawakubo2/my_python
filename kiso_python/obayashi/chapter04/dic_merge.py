countries1 = {"日本": 3, "イギリス": 2}
countries2 = {"チリ": 3, "イギリス": 5}
countries3 = {}
for country, num in countries1.items():
    countries3[country] = num
for country, num in countries2.items():
    countries3[country] = num
print(countries3)
countries = ["フランス", "アメリカ", "中国", "ドイツ", "日本"]

cnt = 0
for country in countries:
    print(str(cnt + 1) + ": " + country)
    cnt += 1 # cnt = cnt + 1

"""
for (int i = 0; i < countries.length; i++) {
    System.out.println(i + ": " + countries[i]);
}
"""
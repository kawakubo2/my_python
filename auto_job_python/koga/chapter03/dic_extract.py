users = {
	"山田太郎" : # name
	{
		"items": [
			[ "05/11", "みかん", 2, 500 ], # date, summary, cnt, price = it
			[ "05/11", "リンゴ", 3, 200 ],
			[ "05/11", "ぶどう", 5, 500 ],
		],
		"total" : 3100
	},
	"横山花子" : {
		"items": [
			[ "05/11", "オレンジ", 3, 300 ],
			[ "05/11", "バナナ", 10, 200 ],
		],
		"total" : 2900
	}
}

for name, data in users.items():
    print(name)
    print(data['total'])
    print(data['items'])
    for item in data['items']:
        hiduke, naiyo, kosu, tanka = item
        print(hiduke)
        print(naiyo)
        print(kosu)
        print(tanka)
        print(kosu * tanka)
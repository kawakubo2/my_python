# -*- coding: utf-8 -*-

students = [ ('田中', 38.2), ('鈴木', 47.2), ('山田', 27.5),  ('横山', 58.0), ('佐藤', 35.7) ]

for num, s in enumerate(sorted(students, key=lambda s: s[1], reverse=True)):
    print("{}:{}({})".format(num + 1, s[1], s[0]))
    
countries = [ 'フランス', 'アメリカ', '中国', 'ドイツ', '日本' ]

for i, country in enumerate(countries):
    print("{}:{}".format(i + 1, country))
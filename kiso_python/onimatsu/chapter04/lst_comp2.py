# -*- coding: utf-8 -*-

lst = [num ** 2 for num in range(0, 21, 2)]

print(lst)

dolls = [1, 5, 9.5, 100]
rate = 101
yens = [doll * rate for doll in dolls]

print(yens)

weekdays = [day + '曜日' for day in '月火水木金土日']

print(weekdays)

nums1 = [1, 3, 7, 10, 9, 15, 20, 30]
nums2 = [n for n in nums1 if n % 3 == 0]
print(nums2)

addresses = ['東京都大田区', '神奈川県横須賀市', '福岡県北九州市',\
'千葉県幕張市', '岡山県倉敷市', '和歌山県和歌山市', '兵庫県神戸市',\
'東京都世田谷区', '神奈川県三浦市', '東京都葛飾区', '神奈川県横浜市']

abc = {'都', '道', '府', '県'}
while True:
    pref = input('都道府県名を入力してください: ')
    if pref[-1] in abc:
        break

cities = [address[len(pref):] for address in addresses if address.startswith(pref)]

print(cities)




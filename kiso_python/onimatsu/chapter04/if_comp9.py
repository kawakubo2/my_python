# -*- coding: utf-8 -*-
import sys

addresses = ['東京都大田区', '神奈川県横須賀市', '福岡県北九州市',\
'千葉県幕張市', '岡山県倉敷市', '和歌山県和歌山市', '兵庫県神戸市',\
'東京都世田谷区', '神奈川県三浦市', '東京都葛飾区', '神奈川県横浜市',\
'福岡県太宰府市', '大阪府堺市', '大阪府大阪市', '東京都品川区']

abc = {'都','道','府','県'}
pref = input('都道府県名を入力してください > ')
if pref[-1] not in abc:
    print('末尾は都・道・府・県を付けてください')
    sys.exit(-1)
ken = [address[len(pref):] for address in addresses if address.startswith(pref)]

print(ken)

names = [('田中一郎', '男'), ('山田太郎', '男'), ('佐藤花子', '女'),
         ('猫山五郎', '男'), ('小林直子', '女'), ('大木虎夫', '男')]

men = [n[0] for n in names if n[1] == '男']
print(men)



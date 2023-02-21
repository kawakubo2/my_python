# -*- coding: utf-8 -*-

shiire = {'高橋昌男', '橋爪健児', '斎藤雅史', '佐々木義夫',
          '矢島美佐子', '内藤友美', '鈴木勝弘', '和田実'}

uriage = {'勝村修平', '高橋昌男', '小島悟', '佐々木義夫',
          '内藤友美', '松本豊彦', '和田実'}

wa = shiire | uriage

print('-- 和集合 ---');
print(wa)

# 仕入担当と売上担当を兼務している人を探す
seki = shiire & uriage
print('--- 積集合 ---')
print(seki)

# 仕入担当専任の人を探す
sa = shiire - uriage
print('--- 差集合 ---')
print(sa)

# 売上担当専任の人を探す
sa2 = uriage - shiire
print('--- 差集合 ---')
print(sa2)

# 仕入担当専任の人と売上担当専任の人を同時に探したい
ha = shiire ^ uriage
print(ha)

cookpad = [{'ジャガイモ', '玉ねぎ', '豚肉'}, {'ブリ', '大根'}, {'ジャガイモ', '玉ねぎ', '人参', 'カレー粉'}]

reizouko = {'ジャガイモ', '玉子', '人参', '豚肉', 'カレー粉', '大根', '玉ねぎ'}

for recipe in cookpad:
    if recipe.issubset(reizouko):
        print(recipe)
        
print('--- 仕入担当専任の人をsetを使わずに解く ---')

shiire = ['高橋昌男', '橋爪健児', '斎藤雅史', '佐々木義夫',
          '矢島美佐子', '内藤友美', '鈴木勝弘', '和田実']

uriage = ['勝村修平', '高橋昌男', '小島悟', '佐々木義夫',
          '内藤友美', '松本豊彦', '和田実']

sa3 = []

for m in shiire:
    if m not in uriage:
        sa3.append(m)
        
print(sa3)


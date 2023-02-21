# -*- coding: utf-8 -*-

print("西暦" + str(2016) + "年は")
print("平成" + str(2016 - 1988) + "年です。")

print("""こんにちは、Python！
時系列分析、機械学習、深層学習、強化学習
いろんなことができます！""")


# 動的型付け言語


prices1 = [100,200,300]
prices2 = prices1
prices2[0] = 1000;

for price in prices1:
    print(price)
    
year1 = 2019 # 10000
year2 = year1 # 20000
year2 = 2020
print('year1=', year1, 'year2=', year2)

num = 10
num = num + 5
print('num=' + str(num))
num += 5
print('num=' + str(num))
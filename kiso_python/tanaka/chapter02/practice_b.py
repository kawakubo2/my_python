# practice_b.py

taro = 170.0
ichiro = 165.5
makoto = 181.5
average = (taro + ichiro + makoto) / 3
# print("平均身長: " + str(average) + "cm")
print("平均身長: {:.1f}cm".format(average))

name = '山田太郎'
bmi = 23.892163
money = 1352352341
print("{}さんのbmi値:{:.1f}".format(name, bmi))
print(f"{name}さんのbmi値:{bmi:.1f}, 貯金額は{money:,}")
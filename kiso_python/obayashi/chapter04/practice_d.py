customers = [("田中一郎", 25),("山田太郎", 23),("佐藤花子", 15),
             ("猫山五郎", 33),("小林直子", 26),("大木虎夫", 18)]

names = [c[0] for c in customers if c[1] >= 20]
print(names)
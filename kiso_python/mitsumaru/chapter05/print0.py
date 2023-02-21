name = "Taro Yamada"
weight = 80
height = 178

print(name + "さんのBMI値は" + str(weight / (height/100) ** 2) + "です。")
print("%sさんのBMI値は%.1fです." % (name, (weight / (height/100) ** 2)))
print("{:12}さんのBMI値は{:.1f}です。".format(name, (weight/(height/100)**2)))
print(f"{name}さんのBMI値は{(weight/(height/100)**2):.1f}です")

score = [81, 78, 62, 100, 52]

for n in score:
    print("{:3} ".format(n), end="")
print()
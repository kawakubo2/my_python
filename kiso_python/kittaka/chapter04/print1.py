name = "山田太郎"
weight = 78
height = 175

# 1
print(name + "さんのBMI値は" + str(weight / (height / 100) ** 2))

# 2
print("%sさんのBMI値は%.1f" % (name, weight / (height / 100) ** 2))

# 3
print("{}さんのBMI値は{:.1f}".format(name, weight / (height / 100) ** 2))

# 4
print(f"{name}さんのBMI値は{weight / (height / 100) ** 2:.1f}")

name1 = "山田"
name2 = "田中"

print("{1}さん、{0}です。...あれ？{1}さんですよね？".format(name1, name2))
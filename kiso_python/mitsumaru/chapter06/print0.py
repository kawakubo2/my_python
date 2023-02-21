name = "山田太郎"
weight = 70
height = 172

print(name + "さんのBMI値は" + str(weight / (height/100) ** 2))
print("%sさんのBMI値は%.1f" % (name, (weight / (height/100) ** 2)))
print("{}さんのBMI値は{:.1f}".format(name, (weight / (height/100) ** 2)))
print(f"{name}さんのBMI値は{weight / (height/100) ** 2:.1f}")
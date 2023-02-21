def addSan(name):
    return name + "さん"

print("こんにちは" + addSan("山田"))

def removeSan(name):
    return name.removesuffix("さん")

s = removeSan("田中さん")
print(s)

def removeHoujinkaku(companyName):
    companyName = companyName.removeprefix("株式会社")
    companyName = companyName.removesuffix("株式会社")
    companyName = companyName.removeprefix("有限会社")
    companyName = companyName.removesuffix("有限会社")
    return companyName

companies = ["株式会社福岡商事", "博多運送株式会社", "駅前有限会社", "有限会社大濠"]
for company in companies:
    print(removeHoujinkaku(company))
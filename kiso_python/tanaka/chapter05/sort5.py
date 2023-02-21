names = {"Taro": 55, "Makoto": 49, "Akio": 30,
         "Kazuo": 32, "Chie": 22, "Ken": 48}

"""
for name, age in sorted(names.items(), key=lambda n: n[0]):
    print(name, age)
for name, age in sorted(names.items()):
    print(name, age)
"""
for name, age in sorted(names.items(), key=lambda n: n[1]):
    print(name, age)
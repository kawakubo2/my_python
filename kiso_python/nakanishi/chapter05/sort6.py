names = {"Taro": 55, "Makoto": 49, "Akio": 30, 
         "Kazuo": 32, "Chie": 22, "Ken": 48}

print('--- 辞書をキー順にソート ---')
for name, age in sorted(names.items()):
    print(f"{name:6}: {age}")
print('--- 辞書を値順にソート ---')
for name, age in sorted(names.items(), key=lambda n: n[1]):
    print(f"{name:6}: {age}")
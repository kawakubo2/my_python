names = {"Taro": 55, "Makoto": 49, "Akio": 30, "Kazuo":32,
         "Chie": 22, "Ken": 48, "Akiko": 30, "Kazuko": 32, "Masako": 49}
print("明示的にキーを指定")
for name, age in sorted(names.items(), key=lambda n: n[0]):
    print(name, age)

print("辞書の場合、暗黙的にキーでソートするため指定は不要")
for name, age in sorted(names.items()):
    print(name, age)

print("値順にソートしたい場合、keyに関数を渡す")
for name, age in sorted(names.items(), key=lambda n: n[1]):
    print(name, age)

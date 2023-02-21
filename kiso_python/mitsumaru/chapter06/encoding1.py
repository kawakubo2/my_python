name = input("名前を入力してください: ")

for n in name:
    print(f"{n}のコードポイントは{ord(n)}")
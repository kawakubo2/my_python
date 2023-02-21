while True:
    bloodtype = input('血液型を入力してください: ')
    if bloodtype in {"a", "b", "o", "ab", "A", "B", "O", "AB"}:
        break
    else:
        print("血液型はA、B、O、ABです。")

bloodtype = bloodtype.upper()
print(f"血液型は{bloodtype}型ですね。")
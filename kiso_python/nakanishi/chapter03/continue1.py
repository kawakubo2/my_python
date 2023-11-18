words = ["旅行", "桜", "鞄", "NG", "テレビ", "NG", "岸辺", "NG", "ギター", "ラジオ"]

for word in words:
    if word == "NG":
        continue
    print(word)

scores = [70, 83, 60, 0, 100, 93, -5, 67, 120, 78]

for score in scores:
    if score < 0 or score > 100:
        print("範囲外の数値です。", score)
        continue
    print(score)
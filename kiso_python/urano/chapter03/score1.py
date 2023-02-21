# score1.py
score = int(input("点数を入力してください: "))

"""
80以上の場合、「合格」
80未満の場合、「不合格」
"""

print("合格" if score >= 80 else "不合格")

if score >= 80:
    print("合格")
else:
    print("不合格")

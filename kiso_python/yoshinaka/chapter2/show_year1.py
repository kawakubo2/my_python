print("西暦" + str(2016) + "年は", end="")
print("平成" + str(2016 - 1988) + "年です。")

s1 = """
こんにちは
Pythonの世界へ
ようこそ
"""
print(s1)

def add(a, b):
    """
    この関数は数値型の2つの引数を
    受取り、その和を求める関数です。
    """
    return a + b

help(add)

print(add(100, 200))
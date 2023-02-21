print("""こんにちは
Pythonの世界へ
ようこそ""")

"""
これは複数行
コメントです。
"""


def add(x, y):
    """
    数値型の2つの引数の和を返す関数
    Args:
        {float}: 加算される数値
        {float}: 加算される数値

    Returns:
        {float} : xとyの和
    """
    return x + y

print(add(13.4, 7.5))
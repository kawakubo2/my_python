def get_rectangle_area(width, height):
    if type(width) not in (int, float):
        raise ValueError("幅が数値ではない")
    if type(height) not in (int, float):
        raise ValueError("高さが数値ではない")
    if width <= 0:
        raise ValueError("幅が負")
    if height <= 0:
        raise ValueError("高さが負")
    return width * height

"""
関数化のメリット
1.繰り返し記述するコードを1つにまとめ、importすることで利用できるようになる
2.名前を付けることにより、処理内容が分かりやすくなる
3.引数チェックが行える
"""
    
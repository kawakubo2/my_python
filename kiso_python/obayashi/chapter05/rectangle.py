def rectangle_area(width, height):
    if type(width) not in (int, float):
        raise ValueError("幅が数値型ではありません")
    if type(height) not in (int, float):
        raise ValueError("高さが数値型ではありません")
    if width < 0 or height < 0:
        raise ValueError("0以上の値を指定してください")

    return width * height

print(rectangle_area(12.5, 8))
print(rectangle_area(height = 20, width = 10))
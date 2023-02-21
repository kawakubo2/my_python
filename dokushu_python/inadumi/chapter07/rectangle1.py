def rectangle_area(width, height):
    if type(width) != int and type(height) != float:
        raise ValueError('幅が数値ではない')
    if width <= 0:
        raise ValueError('幅が0以下')
    if type(height) != int and type(height) != float:
        raise ValueError('高さが数値ではない')
    if height <= 0:
        raise ValueError('高さ0以下')
    return width * height

try:
    print(rectangle_area(10, 7))
except ValueError as ve:
    print(ve)
try:
    print(rectangle_area(-10, 7))
except ValueError as ve:
    print(ve)
try:
    print(rectangle_area('12', 7))
except ValueError as ve:
    print(ve)
import math

RADIUS = 1

width = RADIUS * 2 # 直径 

div_num = 8

def calc_circle_area(width, num):
    width /= div_num
    half_area = 0
    x = -RADIUS + width
    for _ in range(num):
        y = (RADIUS ** 2 - x ** 2) ** 0.5
        half_area += width * y
        x += width
    return half_area * 2
        
DELTA = 1.0e-10
print(f"半径が{RADIUS}の円の面積は{RADIUS ** 2 * math.pi}")
while True:
    temp_area = calc_circle_area(width, div_num)
    print(f"{div_num}分割: {temp_area}")
    if abs(temp_area - RADIUS ** 2 * math.pi) <= DELTA:
        break
    div_num *= 8
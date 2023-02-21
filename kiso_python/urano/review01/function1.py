# function1.py

def calc_gas_price(litter, unit_price, is_member, discount):
    """
    レギュラーガソリンの料金を求める関数。
    Args:
        litter ([float]): [給油したリットル]
        unit_price ([int]): [1リットル当たりの料金]
        is_member (bool): [会員かどうかの判定]
        discount ([int]): [会員の場合の1リットル当たりの割引額]
    Returns:
        int 料金
    """
    pass

price = calc_gas_price(20, 170, True, 3)

def max2(num1, num2):
    """
    2つの数値型の引数のうち大きい数値を返す関数
    Args:
        num1 ([float]): [数値1]
        num2 ([float]): [数値2]
    Returns:
        float 大きい方の数値
    """
    if num1 >= num2:
        return num1
    else:
        return num2
    
print(max2(7, 9))
print(max2(-7, -9))
print(max2(12.34, 12.345))

def max3(num1, num2, num3):
    """
    3つの数値型の引数のうち一番大きい数値を返す関数
    Args:
        num1 ([float]): [数値1]
        num2 ([float]): [数値2]
        num3 ([float]): [数値3]
    Returns:
        float 一番大きい方の数値
    """
    # if num1 >= num2:
    #     if num1 >= num3:
    #         return num1
    #     else:
    #         return num3
    # else:
    #     if num2 >= num3:
    #         return num2
    #     else:
    #         return num3
    return max2(max2(num1, num2), num3)
        
print(max3(1, 2, 3))
print(max3(1, 3, 2))
print(max3(2, 1, 3))
print(max3(2, 3, 1))
print(max3(3, 1, 2))
print(max3(3, 2, 1))

def max4(num1, num2, num3, num4):
    """
    4つの数値型の引数のうち一番大きい数値を返す関数
    Args:
        num1 ([float]): [数値1]
        num2 ([float]): [数値2]
        num3 ([float]): [数値3]
        num4 ([float]): [数値4]
    Returns:
        float 一番大きい方の数値
    """
    return max2(max2(num1, num2), max2(num3, num4))

print(max4(1, 2, 3, 4))
print(max4(1, 2, 4, 3))
print(max4(1, 3, 2, 4))
print(max4(1, 3, 4, 2))
print(max4(1, 4, 2, 3))
print(max4(1, 4, 3, 2))
print(max4(2, 1, 3, 4))
print(max4(2, 1, 4, 3))
print(max4(2, 3, 1, 4))
print(max4(2, 3, 4, 1))
print(max4(2, 4, 1, 3))
print(max4(2, 4, 3, 1))
print(max4(3, 1, 2, 4))
print(max4(3, 1, 4, 2))
print(max4(3, 2, 1, 4))
print(max4(3, 2, 1, 4))
print(max4(3, 4, 1, 2))
print(max4(3, 4, 2, 1))
print(max4(4, 1, 2, 3))
print(max4(4, 1, 3, 2))
print(max4(4, 2, 1, 3))
print(max4(4, 2, 3, 1))
print(max4(4, 3, 1, 2))
print(max4(4, 3, 2, 1))

def my_max(*nums):
    max = nums[0]
    for n in nums:
        if n > max:
            max = n
    return max

print(my_max(5, 9, -3, 12, 6, 7, 10))

def get_triangle_area(base, height):
    return base * height / 2

area = get_triangle_area(10, 8)
print(f"三角形の面積: {area}")

import math

def get_circle_area(radius):
    return math.pow(radius, 2) * math.pi

hankei = 10
print(f"半径が{hankei}の円の面積: {get_circle_area(hankei):.2f}")


     
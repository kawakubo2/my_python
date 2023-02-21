def trapezoid_area(upperbase, lowerbase, height):
    return (upperbase + lowerbase) * height / 2

print(trapezoid_area(4, 6, 5))

print(trapezoid_area(upperbase=4,lowerbase=6,height=5))
print(trapezoid_area(lowerbase=6,height=5,upperbase=4))

def trapezoid_area2(**dic):
    return (dic['upperbase'] + dic['lowerbase']) * dic['height'] / 2

print(trapezoid_area2(height=5,upperbase=4,lowerbase=6))
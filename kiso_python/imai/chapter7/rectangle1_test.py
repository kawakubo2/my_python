from rectangle import Rectangle

r1 = Rectangle(4, 3)
r2 = Rectangle(8, 6)

print("幅が{}、高さが{}の面積は{}、対角線の長さは{:.2f}".\
    format(r1.width, r1.height, r1.area(), r1.diagonal()))
print("幅が{}、高さが{}の面積は{}、対角線の長さは{:.2f}".\
    format(r2.width, r2.height, r2.area(), r2.diagonal()))

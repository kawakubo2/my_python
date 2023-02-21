list28 = [
    [ 28,  5,  8, 15,  4 ],
    [  9, 13,  6,  5, 30 ],
    [  7, 12, 18,  6,  9 ]
]

#  28  5  8 15  4  60
#   9 13  6  5 30  63
#   7 12 18  6  9  52
#                 175
total = 0
for numbers in list28:
    subtotal = 0
    for num in numbers:
        print(f"{num:4}", end="")
        subtotal += num
        total += num
    print(f"{subtotal:5}")
        
print(f"{' ' * 20}{total:5}")
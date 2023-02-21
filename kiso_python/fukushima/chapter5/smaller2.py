# -*- coding: utf-8 -*-

smaller = lambda num1, num2: num2 if num1 > num2 else num1

print(smaller(9, 2))
print(smaller(1, 11))

doll_to_yen = lambda doll, rate=105: doll * rate
print(doll_to_yen(5))
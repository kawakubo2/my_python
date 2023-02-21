# -*- coding: utf-8 -*-

def doll_to_yen(doll, rate=100):
    return doll * rate

doll1 = 100
yen = doll_to_yen(doll1, 105)
print("為替レート: {}".format(105))
print("{}ドルは{}円".format(doll1, yen))

doll2 = 50
yen = doll_to_yen(doll2)
print("為替レート: {}".format(100))
print("{}ドルは{}円".format(doll2, yen))

def daikei(joutei, katei=5, takasa=10):
    return (joutei + katei) * takasa / 2

print(daikei(6, 4, 5))
print(daikei(6, 4))
print(daikei(6))
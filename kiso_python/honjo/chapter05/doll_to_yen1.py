# 関数定義(関数宣言)
def doll_to_yen(doll, rate): # 仮引数(パラメータ)
    return doll * rate

# 関数呼び出し1
yen = doll_to_yen(100, 105)  # 100, 105 <--- 実引数
print("為替レート: {}".format(105))
print("{}ドルは{}円".format(100, yen))

abc = 105
xyz = 100

yen = doll_to_yen(xyz, abc)
print("為替レート: {}".format(abc))
print("{}ドルは{}円".format(xyz, yen))

# =============================================================================
# rate1 = int(input("為替レートを入力してください :"))
# doll1 = int(input("ドルを入力してください: "))
# 
# yen1 = doll_to_yen(doll1, rate1)  # 100, 105 <--- 実引数
# print("為替レート: {}".format(rate1))
# print("{}ドルは{}円".format(doll1, yen1))
# =============================================================================

yen2 = doll_to_yen(doll=100, rate=105)
print("為替レート: {}".format(105))
print("{}ドルは{}円".format(100, yen2))
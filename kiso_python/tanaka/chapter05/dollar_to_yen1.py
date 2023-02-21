import math

def dollar_to_yen(dollar, rate):
    return dollar * rate

r = float(input("為替レート: ")) 
d = float(input("ドル: "))
yen = dollar_to_yen(d, r)
print(f"為替レート: {r}")
print(f"{d}ドルは{math.floor(yen)}円")
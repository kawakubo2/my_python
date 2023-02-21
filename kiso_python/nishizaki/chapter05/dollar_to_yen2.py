def dollar_to_yen(dollar, rate):
    return dollar * rate

yen = dollar_to_yen(dollar=100, rate=105)
print("為替レート: 105")
print(f"100ドルは{yen}円")

r = 100
d = 150
yen = dollar_to_yen(dollar=d, rate=r)
print(f"為替レート: {r}")
print(f"{d}ドルは{yen}円")

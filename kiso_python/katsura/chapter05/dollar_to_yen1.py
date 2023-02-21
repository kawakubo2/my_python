def dollar_to_yen(dollar, rate):
    return dollar * rate

yen = dollar_to_yen(100, 105)
print("為替レート: 105")
print(f"100ドルは{yen}円")

d = 100
r = 150

yen = dollar_to_yen(d, r)
print(f"為替レート: {r}")
print(f"{d}ドルは{yen}円")
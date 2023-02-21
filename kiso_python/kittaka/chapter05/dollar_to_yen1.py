def dollar_to_yen(dollar, rate):
    return dollar * rate

yen = dollar_to_yen(100, 105)
print("為替レート: 105")
print(f"100ドルは{yen}円")

rate = 100
dollar = 150
yen = dollar_to_yen(dollar, rate)
print(f"為替レート: {rate}")
print(f"{dollar}ドルは{yen}円")
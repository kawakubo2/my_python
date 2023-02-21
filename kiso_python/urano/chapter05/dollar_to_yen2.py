def dollar_to_yen(dollar, rate):
    return dollar * rate

yen = dollar_to_yen(rate=105, dollar=100)
print("為替レート: 105")
print(f"100ドルは{yen}円")
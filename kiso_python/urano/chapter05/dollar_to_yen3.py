def dollar_to_yen(dollar, rate=100):
    return dollar * rate

dollar1 = 100
yen = dollar_to_yen(dollar1, 105)
print("為替レート: 105")
print(f"{dollar1}ドルは{yen}円")

dollar2 = 50
yen = dollar_to_yen(dollar2)
print(f"為替レート: 100")
print(f"{dollar2}ドルは{yen}円")
def dollar_to_yen(dollar, rate):
    return dollar * rate

dollar = float(input('ドル: '))
rate = float(input('為替レート: '))

yen = dollar_to_yen(dollar, rate)
print(f"為替レート：{rate}")
print(f"{dollar}は{yen}円")
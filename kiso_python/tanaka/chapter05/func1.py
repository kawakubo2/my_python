import math
def calc_gas_charge(litter, unit_price, member):
    if member == "yes":
        unit_price = unit_price - 3
    return math.floor(litter * unit_price)

litter = float(input("リッター: ")) 
price = int(input("リッター当たりの料金: "))
member = input("会員(yes|no): ")

print(f"レギュラーガソリン{litter}リットルの料金は{calc_gas_charge(litter, price, member)}円です。")
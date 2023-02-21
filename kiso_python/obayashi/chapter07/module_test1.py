from kiso_python.obayashi.chapter07.customer_m1 import Customer

taro = Customer(101, "斎藤太郎", 180)
hanako = Customer(102, "山田花子", 160)

print(f"{taro.name} 標準体重: {taro.std_weight():.2f}kg")
print(f"{hanako.name} 標準体重: {hanako.std_weight():.2f}kg")
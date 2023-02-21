from customer_m1 import Customer

taro = Customer(101, "斉藤太郎", 180)
hanako = Customer(102, "山本花子", 160)

print(f"{taro.number} 標準体重: {taro.std_weight():.2f}kg")
print(f"{hanako.number} 標準体重: {hanako.std_weight():.2f}kg")

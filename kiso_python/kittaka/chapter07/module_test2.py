from customer_m2 import Customer

taro = Customer(101, "斉藤太郎", 180)
print(f"{taro.name} 標準体重: {taro.std_weight():.2f}kg")
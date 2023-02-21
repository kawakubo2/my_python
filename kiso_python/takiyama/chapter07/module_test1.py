import customer_m1

taro = customer_m1.Customer(101, "斉藤太郎", 180)
hanako = customer_m1.Customer(102, "山田花子", 160)

print(f"{taro.name} 標準体重: {taro.std_weight():.2f}kg")
print(f"{hanako.name} 標準体重: {hanako.std_weight():.2f}kg")
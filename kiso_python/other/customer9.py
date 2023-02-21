from customer import GoldCustomer
from datetime import date

taro = GoldCustomer(101, "斉藤太郎", 180, date(1978, 9, 1))

print("{} {} 身長: {}cm 標準体重: {:.2f}kg 生年月日: {}"
	.format(taro.number, taro.name, taro.height, taro.std_weight(), taro.birthdate))
print("年齢: {}".format(taro.get_age()))


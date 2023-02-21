numbers = [0] * 10
print(numbers)
numbers2 = [-1] * 10
print(numbers2)

num = ["zero", "one", "two", "three", "four", "five", "six"]
num1 = num[0:4]
num2 = num[4:]
print(num1)
print(num2)

reverse_num = num[::-1]
print(reverse_num)

str = "Python/Java/Go/Rust/C++/JavaScript"

languages = str.split("/")
print(languages)

date1 = '2021-12-24'
ymd = date1.split("-")
print(ymd)
print(ymd[0])
print(ymd[1])
print(ymd[2])

weekdays = ["日","月","火","水","木","金","土"]
if "月" in weekdays:
    print("月は存在します")
else:
    print("月は存在しません")

for w in weekdays:
    if w == "月":
        print("月は存在します")
        break

if "天" not in weekdays:
    print("天は存在しません")
else:
    print("天は存在します")


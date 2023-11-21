s = "私の会社の郵便番号は、〒812-0013です。"
index = s.find("〒")
print(s[index + 1: index + 9])

email = "tomo.kawakubo@gmail.com"
index = email.find("@")
print(f"ローカル部: {email[:index]}")
print(f"ドメイン部: {email[index + 1:]}")

array = email.split("@")
print(f"ローカル部: {array[0]}")
print(f"ドメイン部: {array[1]}")

ipaddress = "192.168.10.254"
list1 = ipaddress.split(".")
print(list1)

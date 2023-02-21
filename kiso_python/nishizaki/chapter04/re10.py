import re

pattern = "^[0-9]{3}-[0-9]{4}$"
zip1 = "812-0013"
zip2 = "123-45678"

if re.search(pattern, zip1):
    print(f"{zip1}は郵便番号です")
else:
    print(f"{zip1}は郵便番号ではありません")

if re.search(pattern, zip2):
    print(f"{zip2}は郵便番号です")
else:
    print(f"{zip2}は郵便番号ではありません")
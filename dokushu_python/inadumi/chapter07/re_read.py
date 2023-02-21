import re

re1 = re.compile(r'(?<=〒)\d{3}-\d{4}')

str1 = "私の携帯は090-5789-0681で、郵便番号は〒812-0015です。"

results = re1.finditer(str1)
for result in results:
    print(result.group())
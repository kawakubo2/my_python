programmers = [
    {'name': "山田太郎", 'languages': ['Python', 'java', 'C']},
    {'name': "横山花子", 'languages': ['JavaScript', 'Java', 'SQL']},
    {'name': "田中一郎", 'languages': ['Python', 'Ruby']},
]

lang = "java"

for programmer in programmers:
    for la in programmer['languages']:
        if lang == la.lower():
            print(programmer)
            break

str1 = "kokohadoko"
str2 = "ko"

cnt = str1.count(str2)
print(f"{str1}の中に{str2}は{cnt}個あります。")

files = ["aaa.py", "bbb.c", "ccc.java", "ddd.py", "eee.py"]
for file in files:
    if file.endswith(".py"):
        print(file)

urls = ["http://abc.com", "https://www.bbb.jp", 
        "http://example.com", "HTTPS://haru-idea.jp"]

for url in urls:
    if url.lower().startswith("https"):
        print(url)

email = "tomo@kawakubo@gmail.com"
if '@' in email:
    pos = email.index('@')
    if '@' in email:
        pos = email.index('@', pos+1)
        print(f"ローカル部: {email[:pos]}")
        print(f"ドメイン部: {email[pos+1:]}")

if '@' in email:
    pos = email.rfind('@')
    print(f"ローカル部: {email[:pos]}")
    print(f"ドメイン部: {email[pos+1:]}")

names = ["山田太郎", "横山花子", "田中一郎"]
print("---".join(names))

print("kokohadoko".replace("ko", "★"))
name = "山田 太郎"
print(len(name.replace(' ', '')))

numbers = [
    "10,20,30,40,50",
    "11,21,31,41,51",
    "12,22,32,42,52"
]

total = 0
for nums_str in numbers:
    nums_list = nums_str.split(',')
    sub_total = 0
    for num in nums_list:
        sub_total += int(num)
    print(sub_total)
    total += sub_total
print(total)

files = ["aaa.py", "bbb.py", "ccc.py"]
for file in files:
    print(file.removesuffix(".py"))

urls = ["https://abc.com", "https://xyz.ne.jp", "https://lmn.co.jp"]
for url in urls:
    print(url.removeprefix("https://"))

weekdays = "日月火水木金土"
for w in weekdays:
    print(f"{w}曜日")

name = "川久保智晴"
for c in name:
    print(f"{c}の文字コードは{ord(c)}")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

start = 0
step = 5
while True:
    if start + step >= len(alphabet):
        print(alphabet[start: len(alphabet)])
        break
    print(alphabet[start: start+step])
    start += step

print(alphabet[::3])
print(alphabet[1::3])
print(alphabet[2::3])

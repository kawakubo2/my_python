s1 = "kokohagoko"

search = "ko"

count = s1.count(search)
print(f"{s1}の中に{search}は{count}個含まれています。")

files = ["aaa.bbb.ccc.java", "ddd.eee.py", "fff.js", "ggg.hhh.py",
         "iii.c", "jjj.kkk.py"]

for file in files:
    if file.endswith(".py"):
        print(file)

email = "tomo.kawakubo@gmail.com"
pos = email.find("@")
if pos >= 0:
    print(email[:pos])
else:
    print("文字列はEメールアドレスではありません")

if "@" in email:
    print("Eメールアドレスです")
else:
    print("Eメールアドレスではありません")

langlist = ["Python", "Java", "JavaScript", "C++", "C#"]

print(",".join(langlist))

s2 = "AbCdEfGh"
print(f"{s2.lower()}, {s2.upper()}")

s3 = "Yamada,Suzuki,Tanaka,Yamaguchi"
list1 = s3.split(",")
print(list1)

url = "https://example.com"

print(f"{url.removeprefix('https://')}")

file = "abc.xyz.xlsx"

print(f"{file.removesuffix('.xlsx')}")
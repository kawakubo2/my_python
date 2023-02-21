# count メソッド
s1 = "kokohadoko"
c1 = s1.count("ko")
print(s1 + "の文字列の中に" + "ko" + "は" + str(c1) + "回出現します")

# startswith
s2 = "Pythonによるスクレイピング"
b1 = s2.startswith("Python")
if b1:
    print(s2 + "はPythonで始まっています")
else:
    print(s2 + "はPythonで始まっていません")

s3 = "long_long.py"
if s3.endswith(".py"):
    print(s3 + "はPythonファイルです")
else:
    print(s3 + "はPythonファイルではありません")

files = ["abc.java", "def.py", "ghi.php", "jkl.py"]
for file in files:
    if file.endswith(".py"):
        print(file)
    
# splitメソッド
s4 = "札幌,東京,名古屋,大阪,福岡"
list1 = s4.split(",")
print(list1)

s5 = ":".join(list1)
print(s5)

# findメソッド
s6 = "taro.yamada@gmail.com"
p1 = s6.find("@")
print(p1)
    
s7 = "山田太郎"
print(s7[2])

s8 = "川久保智晴"
for c in s8:
    print(c + "の文字コードは" + str(ord(c)))

s9 = "ぁあぃいぅうぇえぉお"
for c in s9:
    print(c + "の文字コードは" + str(ord(c)))
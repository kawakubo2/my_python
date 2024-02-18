import sys

s1 = input("文字列: ")
index = int(input("取り出す位置: "))
if index < 0 or index >= len(s1):
    print("範囲外の位置を指定しています")
    sys.exit()
print(s1[index])
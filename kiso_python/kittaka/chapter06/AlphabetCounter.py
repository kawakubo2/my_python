import os, time

filepath = os.path.join(os.path.dirname(__file__), 'The_Return_of_the_Native_pg122.txt')

f = open(filepath, "r", encoding="utf_8")

start = time.time()
Anum = ord('A') # ordは文字を文字コード(数字)へ変換数関数
Znum = ord('Z')
anum = ord('a')
znum = ord('z')

counter = {} # アルファベットをカウントするための辞書
for num in range(Anum, Znum + 1):
    counter[chr(num)] = 0 # chrは文字コード(数値)を文字へ変換する関数
for num in range(anum, znum + 1):
    counter[chr(num)] = 0
print(counter)

for line in f:
    for c in line:
        if c in counter:
            counter[c] += 1

end = time.time()
for c, num in counter.items():
    print(f"{c}: {num:5d}")
        
print(f"処理時間: {end - start}")

f.close()
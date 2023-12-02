import math

list1 = ["春", "夏", "秋", "冬"]
list1.reverse()
print(list1)

list2 = ["バナナ", "リンゴ", "ナシ", "ブドウ", "メロン"]
# C言語などのreverse関数またはメソッドを持たない言語の解き方
for i in range(math.floor(len(list2) / 2)):
    tmp = list2[i]
    list2[i] = list2[len(list2) - 1 - i]
    list2[len(list2) - 1 - i] = tmp
print(list2)
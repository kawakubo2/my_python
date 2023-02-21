list29 = [
    { "国語": 70, "数学": 82, "英語": 68, "理科": 65, "社会": 75 },
    { "国語": 58, "数学": 92, "英語": 73, "理科": 60, "社会": 67 },
    { "国語": 90, "数学": 58, "英語": 88, "理科": 52, "社会": 72 }
]

# 国語 数学 英語 理科 社会  合計
#  70   82   68  65  75    360
#  58   92   73  60  67    350
#  90   58   88  52  72    360
# 218  232  229 177 214   1070

total = 0
kamoku_total = {"国語": 0, "数学": 0, "英語": 0, "理科": 0, "社会": 0}
print(" ", end="")
for kamoku, _ in kamoku_total.items():
    print(f" {kamoku}", end="")
print("  合計")
print("-" * (5 * 5 + 6))
for scores in list29:
    subtotal = 0
    for kamoku, score in scores.items():
        print(f"{score:5}", end="")
        kamoku_total[kamoku] += score
        subtotal += score
        total += score
    print(f"{subtotal:6}")
print("-" * (5 * 5 + 6))
for _, score in kamoku_total.items():
    print(f"{score:5}", end="")
print(f"{total:6}")


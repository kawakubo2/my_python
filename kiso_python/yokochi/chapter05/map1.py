def to_cm(inch):
    return inch * 2.54

inches = [9, 5.5, 6, 4, 5, 6.5, 10]

"""
関数を引数として取る関数、または関数を戻り値
とする関数を高階関数(higher order function)と呼ぶ
"""
for cm in map(to_cm, inches):
    print(cm)

cms = []
for inch in inches:
    cms.append(to_cm(inch))

print(cms)

for cm in map(lambda inch: inch * 2.54, inches):
    print(cm)
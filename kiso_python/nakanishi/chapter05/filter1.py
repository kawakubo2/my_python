def larger_5(inch):
    return inch > 5

inches = [9, 5.5, 6, 4, 5, 6.5, 10]
cms = []
for inch in filter(larger_5, inches):
    cms.append(inch * 2.54)
print(cms)

print("---< lambda関数を使用 >---")
cms2 = []
for inch in filter(lambda n: n > 5, inches):
    cms2.append(inch * 2.54)
print(cms2)

print("---< 内包表記を使用 >---")
cms3 = [inch * 2.54 for inch in inches if inch > 5]
print(cms3)
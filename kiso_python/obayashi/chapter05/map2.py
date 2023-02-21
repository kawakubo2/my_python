def to_cm(inch):
    return inch * 2.54

inches = [9, 5.5, 6, 4, 6.5, 10]
cms = list(map(to_cm, inches))
print(cms)

cms2 = list(map(lambda inch: inch * 2.54, inches))
print(cms2)

cms3 = [inch * 2.54 for inch in inches]
print(cms3)
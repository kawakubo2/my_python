list17 = [
    [ 70, 50, 78, 90, 83 ],
    [ 68, 75, 84, 80, 72 ],
    [ 90, 68, 62, 92, 48 ],
]

class_total = 0
for student_score in list17:
    student_total = 0
    for score in student_score:
        student_total += score
        print(f"{score:3} ", end="")
    print(f"{student_total:4}")
    class_total += student_total
print(f"{' ' * 20}{class_total}")

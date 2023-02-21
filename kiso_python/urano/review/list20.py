list20 = [
    {'name': '山田太郎', 'score': [70, 62, 83]},
    {'name': '横山花子', 'score': [68, 88, 80]},
    {'name': '田中一郎', 'score': [62, 73, 92]},
]

# 山田太郎 70 62 83 215
# 横山花子 68 88 80 236
# 田中一郎 62 73 92 227

for student_score in list20:
    print(f"{student_score['name']} ", end="")
    student_total = 0
    for score in student_score['score']:
        student_total += score
        print(f"{score:4}", end="")
    print(f"{student_total:5}")

        
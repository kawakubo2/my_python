list21 = [
    {'name':'山田太郎', 'score': {'kokugo': 70, 'sugaku': 62, 'eigo': 83}},
    {'name':'横山花子', 'score': {'kokugo': 68, 'sugaku': 88, 'eigo': 80}},
    {'name':'山田太郎', 'score': {'kokugo': 62, 'sugaku': 73, 'eigo': 92}},
]

for student_score in list21:
    print(student_score['name'], end="")
    student_total = 0
    for kamoku, score in student_score['score'].items():
        student_total += score
        print(f"{score:4}", end="")
    print(f"{student_total:5}")
students = {"山田五郎": 80, "江藤肇": 92, "後藤信": 44,
    "芹沢花子": 82, "伊橋和雄": 98, "太田敬一": 62, "桜井裕": 56,
    "井川一郎": 44, "桜田一": 75, "堀切一郎": 50}

for student in sorted(students.items(), key=lambda n: n[1], reverse=True):
    print("{}: {}".format(student[0], student[1]))

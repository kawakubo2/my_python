students = {"山田五郎": 80, "江藤肇": 92, "後藤信": 44,
            "芹沢花子": 82, "伊橋和雄": 98, "太田敬一": 62,
            "桜井裕": 56, "井川一郎": 44, "桜田一": 75,
            "堀切一郎": 59}

for name, score in sorted(students.items(), key=lambda s: s[1], reverse=True):
    print(f"{name}: {score}")
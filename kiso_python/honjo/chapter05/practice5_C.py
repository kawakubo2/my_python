# -*- coding: utf-8 -*-

students = {"山田五郎": 80, "江藤肇": 92, 
            "後藤信": 44, "芹沢花子": 82}

print(students.items())

for student in sorted(students.items(),
    key=lambda student: student[1], reverse=True):
    print(student[0], student[1])
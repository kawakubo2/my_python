# -*- coding: utf-8 -*-

print('---< タプル >---')
students = [
    ('山田太郎', [72, 78, 48]),
    ('横山花子', [82, 78, 65]),
    ('田中一郎', [34, 100, 91]),
    ('星山裕子', [43, 74, 82])        
]

for student in sorted(students, key=lambda student: sum(student[1]), reverse=True):
    print(student[0], sum(student[1]))
    
    
print('---< 辞書 >---')
students = [
    {'name':'山田太郎', 'score': [83, 43, 53]},
    {'name':'横山花子', 'score': [62, 78, 52]},
    {'name':'田中一郎', 'score': [67, 73, 51]},
    {'name':'星山裕子', 'score': [72, 57, 75]}        
]

for student in sorted(students, key=lambda student: sum(student['score']), reverse=True):
    print(student['name'], sum(student['score']))
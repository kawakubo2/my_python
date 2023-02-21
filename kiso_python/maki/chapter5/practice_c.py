# -*- coding: utf-8 -*-

students = { '山田五郎': 80, '江藤肇': 92, '後藤信': 44, '芹沢花子': 82,
             '伊橋和雄': 98, '太田敬一': 62, '桜井裕': 56, '井川一郎': 44,
             '桜田一': 75, '堀切一郎': 59}

# =============================================================================
# students = { 'Yamada': 80, 'Eto': 92, 'Goto': 44, 'Serizawa': 82,
#              'Ihashi': 98, 'Ohta': 62, 'Sakurai': 56, 'Igawa': 44,
#              'Sakurada': 75, 'Horikiri': 59}
# =============================================================================


for student in sorted(students.items(), key=lambda student: student[1], reverse=True):
    print("{:10s} {:3d}".format(student[0], student[1]))
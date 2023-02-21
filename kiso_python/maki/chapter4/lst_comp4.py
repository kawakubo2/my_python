# -*- coding: utf-8 -*-

weekdays = [day + '曜日' for day in '月火水木金土日']
print(weekdays)

weekdays_list = ['月', '火', '水', '木', '金', '土', '日']
weekdays_youbi_list = [day + '曜日' for day in weekdays_list]
print(weekdays_youbi_list)

weekdays_sun = weekdays_list[-1:] + weekdays_list[:-1]
print(weekdays_sun)
weekdays_sun_youbi = [day + '曜日' for day in weekdays_sun]
print(weekdays_sun_youbi)


files = ['aaa.java', 'bbb.py', 'ccc.php', 'ddd.ruby',
         'eee.c', 'fff.cpp', 'ggg.py', 'hhh.js']

# pythonのリストが欲しい
python_files = [f for f in files if f[-3:] == '.py']
print(python_files)

import glob

python_files2 = [f for f in glob.glob('*.*') if f[-3:] == '.py']
print(python_files2)
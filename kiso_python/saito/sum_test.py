# -*- coding: utf-8 -*-

numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

numbers[3] = 100

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        print(numbers[i])
        
for num in numbers:
    print(num)


weekday = {'日': 'Sun', '月': 'Mon', '火': 'Tue',
           '水': 'Wed', '木': 'Thu', '金': 'Fri', '土': 'Sat'}

print(weekday['金'])

employee_list = {101: {'name': '山田太郎', 'age': 25},
                 102: {'name': '横山花子', 'age': 34},
                 103: {'name': '田中一郎', 'age': 55},
                 104: {'name': '山本久美子', 'age': 42}}

emp_no = int(input('社印番号: '))

employee = employee_list[emp_no]
print("名前:{} 年齢:{}".format(employee['name'], employee['age']))
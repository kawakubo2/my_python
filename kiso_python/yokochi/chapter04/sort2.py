clazz = ['部長', '課長', '主任', '担当']

employees = [
    {'name': '田中一郎', 'age': 38, 'class': '課長'},
    {'name': '星山裕子', 'age': 32, 'class': '主任'},
    {'name': '鈴木次郎', 'age': 45, 'class': '部長'},
    {'name': '佐藤勝男', 'age': 28, 'class': '担当'},
    {'name': '横山花子', 'age': 35, 'class': '課長'}
]

sorted_employees = sorted(employees, key=lambda e: clazz.index(e.get('class')))
for employee in sorted_employees:
    print(employee)
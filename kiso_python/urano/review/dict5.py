
def get_employee(emp_no):
    employees = {
        '1001': {'name': '山田太郎', 'age': 28},
        '1002': {'name': '横山花子', 'age': 41},
        '1003': {'name': '田中一郎', 'age': 56},
        '1004': {'name': '山本久美子', 'age': 35},
        '1005': {'name': '鈴木次郎', 'age': 44},
        '1006': {'name': '星山裕子', 'age': 25},
        '1007': {'name': '佐藤勝男', 'age': 30}
    }
    if emp_no not in employees:
        return None
    return employees[emp_no]

emp = input('社員番号: ')
employee = get_employee(emp)
if employee:
    print(f"{employee['name']} {employee['age']}歳")
else:
    print(f"{emp}は見つかりません。")
    
    
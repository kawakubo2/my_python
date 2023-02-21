import sys, os

with open(os.path.dirname(__file__) + '/employees.txt', 'r', encoding='utf_8') as f:
    employees = f.readlines()

for e in employees:
    name, age, address = e.split(',')
    print(f"{name}\t{age}\t{address}", end='')

while True:
    sw = input("1.追加 2.一覧表示 3.終了")
    if sw == '3':
        sw = input('保存しますか？(y/n): ')
        if sw == 'y':
            with open(os.path.dirname(__file__) + '/employees.txt', 'w', encoding='utf_8') as f:
                f.writelines(employees)
        break
    elif sw == "1":
        name = input('名前: ')
        age = input('年齢: ')
        address = input('住所: ')
        employees.append(f"{name},{age},{address}\n")
    elif sw == "2":
        for e in employees:
            name, age, address = e.split(',')
            print(f"{name}\t{age}\t{address}", end='')
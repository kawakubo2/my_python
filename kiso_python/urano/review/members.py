import os

def read_members():
    members = {}
    with open(os.path.dirname(__file__) + '/members.txt', 'r', encoding='utf_8') as f:
        for line in f:
            [username, name, age, weight, height] = line.rstrip("\n").split(",")
            members[username] = {'name': name, 'age': int(age), 'weight': float(weight), 'height': float(height)}
    return members

def save_members(members):
    with open(os.path.dirname(__file__) + '/members.txt', 'w', encoding='utf_8') as f:
        for username, member in members.items():
            f.write(f"{username},")
            f.write(f"{member['name']},")
            f.write(f"{member['age']},")
            f.write(f"{member['weight']},")
            f.write(f"{member['height']}\n")
            
members = read_members()

while True:
    answer = int(input('1.新規登録 2.検索 3.削除 9.終了: '))
    if answer == 9:
        answer = input('保存しますか?(yes/no): ')
        if answer == 'yes':
            save_members(members)
        break
    if answer == 1:
        new_username = input('新規ユーザ名: ')
        if new_username in members:
            print(f"{new_username}は既に存在します。")
            continue
        name = input('名前: ')
        age = int(input('年齢: '))
        weight = float(input('体重: '))
        height = float(input('身長: '))
        values = {'name': name, 'age': age, 'weight': weight, 'height': height}
        members[new_username] = values
    elif answer == 2:
        username = input('ユーザ名: ')
        if username not in members:
            print(f"{username}は会員ではありません。")
            continue
        member = members[username]
        print(f"ユーザ名: {username} 名前: {member['name']} 体重: {member['weight']}kg 身長: {member['height']}cm")
    elif answer == 3:
        username = input('ユーザ名: ')
        if username not in members:
            print(f"{username}は会員ではありません。")
            continue
        del members[username]
    else:
        print('1, 2, 3から選択してください。')
    print(members)
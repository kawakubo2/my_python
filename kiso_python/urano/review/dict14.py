import os

members = {} 

def get_members():
    global members
    with open(os.path.dirname(__file__) + '/members.txt', 'r', encoding='utf_8') as f:
        member = {}
        for line in f:
            item = line.split(',')
            member['name'] = item[1]
            member['age'] = int(item[2])
            member['weight'] = float(item[3])
            member['height'] = float(item[4])
            members[item[0]] = member
    

def get_member_profile(member_id):
    """
    引数のメンバーIDを元に連想配列からメンバー情報を返す関数
    Args:
        member_id ([str]): [メンバーID]
    """
    global members
    if member_id not in members:
        return None
    return members[member_id]

def print_member(member):
    print(f"名前: {member['name']}")
    print(f"年齢: {member['age']}")
    print(f"体重: {member['weight']}")
    print(f"身長: {member['height']}")

def create_member():
    name = input('名前: ')
    age = int(input('年齢: '))
    weight = float(input('体重(kg): '))
    height = float(input('身長(cm): '))
    return {'name': name, 'age': age, 'weight': weight, 'height': height}

def save_members():
    global members
    with open(os.path.dirname(__file__) + '/members.txt', 'w', encoding='utf_8') as f:
        for id, member in members.items():
            f.write(f"{id},")
            f.write(f"{member['name']},")
            f.write(f"{member['age']},")
            f.write(f"{member['weight']},")
            f.write(f"{member['height']}\n")
    
print('---< メンバー情報検索 >---')
get_members()
while True:
    id = input('メンバーID(終了時はq): ')
    if id == 'q':
        answer = input('保存しますか？(yes/no): ')
        if answer == 'yes':
            save_members()
        break
    member = get_member_profile(id)
    if member:
        print_member(member)
    else:
        print(f"{id}に該当するメンバーは見つかりませんでした。")
        answer = input('追加しますか？(yes/no): ')
        if answer == 'yes':
            new_member = create_member()
            members[id] = new_member
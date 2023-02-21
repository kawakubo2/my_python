usernames = ['abc', 'xyz', 'いろは', '123']

user = input('ユーザ名: ')

"""
flag = True 
for name in usernames:
    if name == user:
        print(f"{user}は既に存在します。")
        flag = False
        break

if flag:
    print(f"{user}は使用可能です。")
"""

for name in usernames:
    if name == user:
        print(f"{user}は既に存在します。")
        break
else:
    print(f"{user}は使用可能です。")
members = [('山田太郎', 40), ('横山花子', 35), ('田中一郎', 55)]

bonus_list = [ m[1] for m in members]
print(bonus_list)

bonus_list2 = []
for m in members:
    bonus_list2.append(m[1])
print(bonus_list2)
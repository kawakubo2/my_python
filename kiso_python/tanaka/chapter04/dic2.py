dic = {'日': 'Sun', '月': 'Mon', '火': 'Tue', '水': 'Wed', '木': 'Thu', '金': 'Fri', '土': 'Sat'}

for ja, en in dic.items():
    print(f"{ja}:{en}")

for ja in dic.keys():
    print(f"{ja}:{dic[ja]}")
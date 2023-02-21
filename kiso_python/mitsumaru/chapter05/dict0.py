score = {"哲学":95, "数学": 94, "物理": 91, "国際法":100,"脳科学": 100, "心理学":98}

def dict_value_max(dic1):
    max = -1 * 2** 64;
    for tensu in dic1.values():
        if tensu > max:
            max = tensu
    return max

print(f"最高点: {dict_value_max(score)}")

def dict_value_min(dic1):
    min = 2** 64
    for tensu in dic1.values():
        if tensu < min:
            min = tensu
    return min

print(f"最低点: {dict_value_min(score)}")
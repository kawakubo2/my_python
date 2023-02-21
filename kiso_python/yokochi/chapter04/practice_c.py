lang = {'Python': 45, 'C': 14, 'Swift': 40, 'JavaScript': 40, 'Java': 44, 'LotusScript': 1}

def str_max_length(ary):
    return max([len(elem) for elem in ary])


for l, n in lang.items():
    print(f"{l:{str_max_length(lang)}}の利用者は{n:2}人")
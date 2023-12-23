lang = {"Python": 45, "C": 14, "Swift": 40, "JavaScript": 40, "Java": 44}
l_max = max([len(l) for l, n in lang.items()])
for l, n in lang.items():
    print("{}の利用者は{}人".format(l, n))
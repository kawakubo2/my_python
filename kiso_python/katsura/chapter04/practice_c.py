lang = {"Python": 44, "C": 14, "Swift": 40, "JavaScript": 40, "Java": 40}
max_length = max([len(s) for s in lang.keys()])
for l, n in lang.items():
    print(f"{l:{max_length}}の利用者は{n}人")
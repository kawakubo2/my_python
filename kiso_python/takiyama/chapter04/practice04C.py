langs = {"Python": 45, "C": 14, "Swift": 40, "JavaScript": 40,
         "Java": 44, "ActionScript": 100}
max_str_len = max([len(lang) for lang in langs])
for lang, num in langs.items():
    print(f"{lang:{max_str_len}}の利用者は{num:4}人")
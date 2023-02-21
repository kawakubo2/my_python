langs = {"Python": 45, "C": 14, "Swift": 40, "JavaScript": 40, "Java": 44 }
maxlength = max([len(lang) for lang in langs.keys()])
for lang, num in langs.items():
    print(f"{lang:{maxlength}}の利用者は{num}人")
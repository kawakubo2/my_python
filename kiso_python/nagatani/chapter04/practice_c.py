langs = {'Python': 45, 'C': 14, 'Swift': 40, 'JavaScript': '40', 'Java': 44, 'FlowDesigner': 1}

lang_list = langs.keys()
max_length = max([len(lang) for lang in langs])

for lang, count in langs.items():
    print(f"{lang:{max_length}}:{count}")
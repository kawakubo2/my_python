langs = {"Python":45,"C":14,"Swift":40,"JavaScript":40,"Java":44}
max_length = max([len(lan) for lan in langs])
for lang, cnt in langs.items():
    print(f"{lang:{max_length}} : {cnt}")
    
print(max([6, 1, 5, 10, 4]))
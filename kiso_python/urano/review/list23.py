langs = ['Java', 'JavaScript', 'Go', 'Python', 'Rust', 'C++'];

keyword = input('プログラム言語: ')

for i, lang in enumerate(langs):
    if lang == keyword:
        pos = i
        break;
else:
    pos = -1
    
if pos != -1:
    print(f"{keyword}はリストの{pos}番目にあります。")
else:
    print(f"{keyword}はリストにありません。")

pos = langs.index(keyword);
if pos != -1:
    print(f"{keyword}はリストの{langs.index(keyword)}番目にあります。")

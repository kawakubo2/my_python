lst1 = ["fly", "good", "ABC", "Bad", "Woo", "Foo", "and"]
lst2 = sorted(lst1, key=str.upper)
print(lst2)

langs = ['Python', 'Java', 'Go', 'C', 'Rust', 'JavaScript', 'C++']

sorted_langs = sorted(langs, key=lambda lang: len(lang), reverse = True)
print(sorted_langs)
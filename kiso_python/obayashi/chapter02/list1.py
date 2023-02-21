lang = ['Python', 'C', 'C++', 'Java', 'C#', 'Go', 'Rust']

lang.append('TypeScript')
print(lang)
temp = lang.pop()
print(temp + "が末尾から削除されました")
print(lang)

print(lang[0:4])
print(lang[4:])
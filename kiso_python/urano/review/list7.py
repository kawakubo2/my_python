list7 = ['A', 'C', 'B', 'X', 'Y', 'A', 'X', 'C', 'A']

c = input('削除したい文字: ')

while c in list7:
    list7.remove(c)
    
print(list7)
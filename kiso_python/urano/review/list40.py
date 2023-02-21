list40 = ['Taro Yamada', 'Hanako Yokoyama', 'Ichiro Tanaka', 'Kumiko Yamamoto']

# 姓と名に分けて表示 例)  姓:Yamada 名:Taro

for name in list40:
    firstname, lastname = name.split(' ')
    print(f"姓: {lastname} 名: {firstname}")
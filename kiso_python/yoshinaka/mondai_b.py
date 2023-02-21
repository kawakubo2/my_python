temp = input('生まれた年を入力してください(1995-11-23): ')
strary = temp.split('-')
intary = [int(s) for s in strary]
birthdate = (intary[0], intary[1], intary[2])

if birthdate < (1989, 1, 7):
    print('昭和以前の生まれですね')
elif birthdate < (2019, 5, 1):
    print('平成生まれですね')
else:
    print('令和生まれですね')
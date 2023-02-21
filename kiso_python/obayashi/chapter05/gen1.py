def my_gen(str):
    for c in str.upper():
        yield c

gen = my_gen("HeLlo")
while True:
    try:
        print(next(gen))
    except:
        break

gen = my_gen("HeLlo")
# 上記構文を簡単に使用できるようにしている
# 糖衣構文(Syntax Sugar)
for c in my_gen("JavaScript"):
    print(c) 
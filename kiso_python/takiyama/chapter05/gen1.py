def my_gen1(s):
    for c in s.upper():
        yield c
        
gen = my_gen1('HeLlo')
print("---< next関数で取り出す方法 >---")
while True:
    try:
        print(next(gen))
    except StopIteration:
        break

gen = my_gen1('HeLlo')
print("---< for inで取り出す方法 >---")
# 糖衣構文(Syntax Sugar)
for c in gen:
    print(c)
def my_gen1(s):
    for c in s.upper():
        yield c
        
gen = my_gen1("HeLlo")
"""
while True:
    try:
        print(next(gen))
    except StopIteration:
        break
"""
# 糖衣構文(Syntax Sugar)
for c in gen:
    print(c)
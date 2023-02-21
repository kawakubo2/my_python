def my_gen1(str):
    for c in str.upper():
        yield c
        
gen = my_gen1("HelLo")     
"""
try:
    while True:
        print(next(gen))
except StopIteration:
    pass
"""
# シンタックスシュガー(糖衣構文)
for n in gen:
    print(n)
def my_gen1(str):
    for c in str.upper():
        yield c

gen = my_gen1("HeLlo")
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
for c in gen:
    print(c)
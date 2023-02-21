def my_gen1(str):
    for c in str.upper():
        yield c

# gen = my_gen1("HeLlo")
# while True:
#     try:
#         print(next(gen))
#     except:
#         break

for c in my_gen1("HeLlo"):
    print(c)
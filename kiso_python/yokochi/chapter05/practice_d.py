def gen_list(lst):
    for u in lst:
        yield u.upper()

lst = ["python", "c", "java", "basic", "swift"]
gen = gen_list(lst)
for s in gen:
    print(s)
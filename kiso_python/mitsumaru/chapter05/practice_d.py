def gen_list(lst):
    for s in lst:
        yield s.upper()

lst = ["python", "c", "java", "basic", "swift"]
gen = gen_list(lst)
for s in gen:
    print(s)
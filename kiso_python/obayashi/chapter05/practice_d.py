def gen_list(lst):
    for s in lst:
        yield s.upper()

langs = ["python", "c", "java", "basic", "swift"]
gen = gen_list(langs)
for s in gen:
    print(s)

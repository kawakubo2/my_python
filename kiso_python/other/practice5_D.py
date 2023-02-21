def gen_list(lst):
    for s in lst:
        yield s

lst = ['Python', 'C', 'Java', 'Basic', 'Swift']

gen = gen_list(lst)

for s in gen:
    print(s)

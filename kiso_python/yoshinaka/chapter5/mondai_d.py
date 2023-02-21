def gen_list(lst):
    for item in lst:
        yield item.upper()

lst = ['python', 'c', 'java', 'basic', 'swift']
gen = gen_list(lst)

for s in gen:
    print(s)
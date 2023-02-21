def gen_list(lst):
    for s in lst:
        yield s.upper()
        
lst = ["python", "c", "java", "basic", "swift"]
gen = gen_list(lst)
for s in gen:
    print(s)

def return_list(lst):
    result = []
    for s in lst:
        result.append(s.upper())
    return result

print('----------')
lst2 = return_list(lst)
for s in lst2:
    print(s)
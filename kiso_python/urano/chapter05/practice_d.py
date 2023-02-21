"""
def gen_list(lst):
    for s in lst:
        yield s.upper()
"""

lst = ["python", "c", "java", "basic", "swift"]
gen = (s.upper() for s in lst)
for s in gen:
    print(s)
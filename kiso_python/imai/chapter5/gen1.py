# -*- coding: utf-8 -*-

def my_gen1(str):
    for c in str.upper():
        yield c
        
def my_gen2(str):
    return str.upper()
        
gen = my_gen1('HeLlo')
# =============================================================================
# while True:
#     try:
#         print(next(gen))
#     except StopIteration:
#         break
# =============================================================================

# シンタックス・シュガー(糖衣構文)
for c in gen:
    print(c)
    
for c in my_gen2('HeLlo'):
    print(c)
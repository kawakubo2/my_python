set1 = { "xyz", "abc", "lmn"}
for s in set1:
    print(s.upper())

list1 = [1, 2, 3, 4, 5, 1, 2]

set2 = set(list1)

print(set2)

members = [12, 11, 1, 2, 1, 2, 12, 20, 23, 1, 11, 20]

set3 = set(members)
print(set3)
print(len(set3))

set4 = frozenset([1, 2, 3])
set3.add(100)

set5 = { 1, 2, 3, frozenset([1, 2, 3])}
print(set5)

print(id(1))

n = 1
print(id(n))

print('ABC')
s = 'ABC'
print(id('ABC'))
print(id(s))

set6 = {1, 2, 3}
set7 = {1, 2, 3}

print(id(set6))
print(id(set7))

set8 = {1, 2, 3, 4, 5, 6, 7, 8}
print(9 in set8)

set10 = { 10, 105, 30, 7}
set11 = { 105, 28, 32, 7}

def my_intersect(set1, set2):
    result = set()
    for n in set1:
        if n in set2:
            result.add(n)
    return result

set11 = my_intersect(set10, set11)
print(set11)

def my_difference(set1, set2):
    result = set()
    for n in set1:
        if n not in set2:
            result.add(n)
    return result

set12 =  my_difference(set10, set11)
print(set12)
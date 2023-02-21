def test2(lst):
    lst[0] = 0
    lst.append(100)
    print(lst)

l = [1, 2, 3]
test2(l)
print(l)
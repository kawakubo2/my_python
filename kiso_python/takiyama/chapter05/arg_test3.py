def test2(lst):
    print(f"lst: {id(lst)}")
    lst[0] = 0
    lst.append(100)
    print(f"lst: {id(lst)}")

l = [1, 2, 3]
test2(l)
print(l)
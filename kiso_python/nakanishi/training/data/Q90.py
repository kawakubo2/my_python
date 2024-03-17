li = ["orange", "apple", "banana", "pineapple", "lemon", "apple", "banana"]

for i in range(len(li) // 2):
    tmp = li[i]
    li[i] = li[len(li) - 1 - i]
    li[len(li) - 1 - i] = tmp

print(li)

li = ["orange", "apple", "banana", "pineapple", "lemon", "apple", "banana"]

for i in range(len(li) // 2):
    tmp = li[i]
    li[i] = li[-i - 1]
    li[-i - 1] = tmp

print(li)
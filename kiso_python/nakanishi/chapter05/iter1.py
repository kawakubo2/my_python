fruits = ["apple", "banana", "orange", "grape"]

print("--- イテレータを使用 ---")
itr = iter(fruits)
while True:
    try:
        print(next(itr))
    except StopIteration:
        break

print("--- for inを使用 ---")
for f in fruits:
    print(f)
    
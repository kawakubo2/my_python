data = [1, 2, 3]
itr = iter(data)
while True:
    try:
        print(next(itr))
    except:
        break

for n in data:
    print(n)

for i in range(len(data)):
    print(data[i])
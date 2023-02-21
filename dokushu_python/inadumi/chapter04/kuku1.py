for i in range(1, 10):
    for j in range(1, 10):
        print('{:2d} '.format(i * j), end='')
    print()

kuku = [i * j for i in range(1, 10) for j in range(1, 10)]
for i, n in enumerate(kuku):
    if i % 9 == 0:
        print()
    print('{:2d} '.format(n), end='')
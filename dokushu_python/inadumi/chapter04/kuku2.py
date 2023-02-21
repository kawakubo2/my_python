counter = 0
for i in range(1, 10):
    for j in range(1, 10):
        counter += 1
        if i * j > 30:
            break
        print('{:2d} '.format(i * j), end='')
    print()
    
print('回数:{}'.format(counter))

for i in range(1, 10):
    for j in range(1, 10):
        if i * j > 30:
            break
        print('{:2d} '.format(i * j), end='')
    else:
        print()
        continue
    break
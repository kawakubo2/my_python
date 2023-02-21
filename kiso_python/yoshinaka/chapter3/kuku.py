counter = 0
for i in range(1, 10):
    for j in range(1, 10):
        counter += 1
        if i * j > 30: break
        print('{:2d}, '.format(i * j), end='')
    print('')

print('{}回'.format(counter))
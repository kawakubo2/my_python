import time, os

start_time = time.time()

alpabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

result = {}

for a in alpabet:
    result[a] = 0

with open(os.path.dirname(__file__) + '/The_Return_of_the_Native_pg122.txt', 'r', encoding='utf_8') as f:
    for line in f:
        line = line.rstrip('\n')
        for c in line:
            if c in result:
                result[c] += 1

for alpha, num in sorted(result.items()):
    print('{}: {:6d}'.format(alpha, num))
    
end_time = time.time()

print('処理時間:', end_time - start_time)
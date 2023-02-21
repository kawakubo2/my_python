import time

start_time = time.time()
lst = []

for num in range(10000000):
    lst.append(num ** 2)

end_time = time.time()
print('処理時間:{}'.format(end_time - start_time))

start_time = time.time()
# リストの内包表記
lst2 = [num ** 2 for num in range(10000000)]
end_time = time.time()

print('処理時間:{}'.format(end_time - start_time))
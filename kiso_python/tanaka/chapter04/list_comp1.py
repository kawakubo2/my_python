lst1 = []
for num in range(0, 21, 2): # 0～20までの偶数
    lst1.append(num ** 2)
    
print(lst1)

lst2 = [num ** 2 for num in range(0, 21, 2)]
print(lst2)

import math
prices = [1000, 500, 800, 700, 1200]
prices2 = [math.floor(p * 1.1) for p in prices]
print(prices2)

prices3 = []
for p in prices:
    prices3.append(math.floor(p * 1.1))
    
print(prices3)
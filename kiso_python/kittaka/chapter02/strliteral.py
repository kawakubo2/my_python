print("I'm teacher.")
print('I\'m "GREAT" \n\n\nteacher')

s1 = "ABCDEF"
s2 = "ァアィイン"

for c in s1:
    print(c, ord(c))
for c in s2:
    print(c, ord(c))

print("Machi Caf\u00E9")
print("\u064a\u0627\u062e\u0634\u0649\u0645\u06c7\u0633\u0649\u0632")

n = 0
s3 = "15"

height = [10, 20, 30, 40, 50]

print(height[len(height) - 1])
print(height[-1])

def group_func(nums):
    total = 0
    cnt = 0
    max = nums[0]
    min = nums[0]
    for n in nums:
        total += n
        if n > max:
            max = n
        if n < min:
            min = n
        cnt += 1
        
    return [total, total / cnt, max, min, cnt]

numbers = [5, 4, 8, 1, 10, 2, 3, 7, 6, 9]

mytotal, myavg, mymax, mymin, mycount = group_func(numbers)

print("合計:", mytotal)
print("平均:", myavg)
print("最大:", mymax)
print("最小:", mymin)
print("件数:", mycount)

print(id(123))
n = 123
print(id(n))
n = 246
print(id(n))

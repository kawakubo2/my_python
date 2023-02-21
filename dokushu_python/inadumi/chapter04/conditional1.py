x = 5
y = 10
z = 8

# () {} [] '' ""
if (x > 10 or 
    y == 10 or 
    z > 4):
    print('xxx')

w = 0
msg = ''

msg = msg or 'とくになし'
print(msg)

set1 = set()

lst = None
lst = lst or []

print(lst)

dict1 = None
dict1 = dict1 or {}

print(dict1)

nums = [1, 2, 3, 4, 5]
for n in nums:
    n *= 2

print(nums)

for i in range(len(nums)):
    nums[i] *= 2

print(nums)
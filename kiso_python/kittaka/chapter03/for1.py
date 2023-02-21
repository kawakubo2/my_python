lst = ["日曜日", "月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日"]

"""
itr = iter(lst)
try:
   while True:
       print(next(itr))
except StopIteration:
    pass
"""

        
# 糖衣構文(Syntax Sugar)
for day in lst:
    print(day)

for i in range(len(lst)):
    print(lst[i])
"""
for (i = 0; i < nums.length; i++) {
    nums[i] *= 2
}
"""    
def double(nums):
    for i in range(len(nums)):
        nums[i] *= 2

numbers = [1, 2, 3]
double(numbers)
print(numbers)
members = ['山田太郎', '横山花子', '田中一郎', '山本久美子', '鈴木次郎', 
    '星山裕子', '佐藤勝男']

for member in members:
    print(member)

for i in range(len(members)):
    print(members[i])

numbers = [1, 2, 3, 4, 5]
numbers[2:4] = [10, 20, 30, 40]

print(numbers)

def nibai(nums):
    for i in range(len(nums)):
        nums[i] *= 2 # nums[i] = nums[i] * 2
nibai(numbers)
print(numbers)

s = "日月火水木金土"
weeks = [c + '曜日' for c in s]
print(weeks)

season = ['春', '夏', '秋', '冬']

iter1 = iter(season)

try:
    while True:
        print(next(iter1))
except:
    pass

# シンタックスシュガー(糖衣構文)
for member in members:
    print(member)
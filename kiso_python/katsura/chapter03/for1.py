names = ['山田太郎', '横山花子', '田中一郎', '山本久美子', '鈴木次郎']

for name in names:
    print(name)

s1 = "日月火水木金土"

for c in s1:
    print(c + '曜日')

def nibai(nums):
    # for n in nums:
    #     n *= 2
    for i in range(len(nums)):
        nums[i] *= 2

numbers = [1, 2, 3]
nibai(numbers)

season = ['春', '夏', '秋', '冬']

itr = iter(season)
while True:
    try:
        print(next(itr))
    except StopIteration:
        break

# 糖衣構文(シンタックスシュガー)
for s in season:
    print(s)
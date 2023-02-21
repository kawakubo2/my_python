countries = ['フランス', 'アメリカ', '中国', 'ドイツ', '日本']

cnt = 0
for country in countries:
    print(str(cnt + 1) + ": " + country)
    cnt += 1

for num in range(len(countries)):
    print(str(num + 1) + ': ' + countries[num])

def double_int(nums):
    for i in range(len(nums)):
        nums[i] *= 2

numbers = [1, 2, 3, 4, 5]
print(numbers)

double_int(numbers)
print(numbers)
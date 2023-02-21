# higher_order_func.py

numbers = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def total1(nums):
    total = 0
    for n in nums:
        total += n
    return total

print(f"合計: {total1(numbers)}")

def total2(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total

print(f"偶数の合計: {total2(numbers)}")

def total3(nums):
    total = 0
    for n in nums:
        if n > 0 and n % 2 == 0:
            total += n
    return total

print(f"正の偶数の合計: {total3(numbers)}")

def higher_total(filter, nums):
    total = 0
    for n in nums:
        if filter(n):
            total += n
    return total

print(f"合計: {higher_total(lambda n: True, numbers)}")
print(f"偶数の合計: {higher_total(lambda n: n % 2 == 0, numbers)}")
print(f"正の偶数の合計: {higher_total(lambda n: n > 0 and n % 2 == 0, numbers)}")

def mymap(func, lst):
    for item in lst:
        yield func(item)

inches = [9, 5.5, 6, 4, 5, 6.5, 10]
for cm in mymap(lambda inch: inch * 2.54, inches):
    print(cm)
    
companies = [('田中', '前', '有限会社'), ('鈴木', '後', '株式会社'), ('山田', '後', '合名会社')]

def make_company_name(company):
    if company[1] == '前':
        result = company[2] + company[0]
    elif company[1] == '後':
        result = company[0] + company[2]
    else:
        result = None
    return result

for company in map(make_company_name, companies):
    print(company)

langs = ['Python', 'PHP', 'Java', 'Rust', 'Go', 'JavaScript']
lst1 = list(filter(lambda n: len(n) > 5, langs))
print(lst1)

lst2 = [lang for lang in langs if len(lang) > 5]
print(lst2)

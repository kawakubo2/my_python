def double1(num):
    num *= 2 # num = num * 2
    print(f"num={num}")
n = 10
double1(n)
print(f"n={n}")

def double2(nums):
    for i in range(len(nums)):
        nums[i] *= 2
    print(nums)

def double3(nums):
    result = []
    for n in nums:
        result.append(n * 2)
    return result
        
numbers = [1, 2, 3]
double2(numbers)
print(numbers)

numbers2 = double3(numbers)
print(numbers2)

today_sales = [100000, 50000, 30000, 200000, 300000]
"""
def addTax(sales):
    for i in range(len(today_sales)):
        today_sales[i] *= 1.1

def addTax2(sales):
    result = []
    for price in sales:
        result.append(price * 1.1)
    return result

today_sales_with_tax = addTax2(today_sales)
print(today_sales) 
print(today_sales_with_tax) 
"""
sales3 = [price * 1.1 for price in today_sales]
print(sales3)
print(today_sales)
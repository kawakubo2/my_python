def test1(num):
    num += 10
    print("num={}".format(num))
    
    
n = 3
test1(n)
print("n={}".format(n))

def test2(numbers):
    numbers[0] = 100
    
    
nums = [1, 2, 3, 4, 5, 6]
test2(nums)
print(nums)
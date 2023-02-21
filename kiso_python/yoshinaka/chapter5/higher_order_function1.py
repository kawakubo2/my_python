numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

def my_sum(nums):
    total = 0
    for n in nums:
        total += n
    return total

print(my_sum(numbers))

def positive_sum(nums):
    total = 0
    for n in nums:
        if n > 0:
            total += n
    return total

print(positive_sum(numbers))

def positive_even_sum(nums):
    total = 0
    for n in nums:
        if n > 0 and n % 2 == 0:
            total += n
    return total

print(positive_even_sum(numbers))

def hof_sum(func, nums):
    """
    引数で受け取った整数のリストからfunc関数で真となる要素だけの合計
    を求め、戻り値として返す関数
    func : 整数を引数として取り、真偽値型を戻す関数
    nums : 整数のリスト 
    """
    total = 0
    for n in nums:
        if func(n):
            total += n
    return total

print(hof_sum(lambda n: n > 0, numbers))
print(hof_sum(lambda n: n > 0 and n % 2 == 0, numbers))
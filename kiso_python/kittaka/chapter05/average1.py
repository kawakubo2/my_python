def average(*nums):
    """
    引数は数値型が1個以上必要
    Returns:
        _type_: _description_
    """
    return sum(nums) / len(nums)

print(average(1, 10, 100))
print()

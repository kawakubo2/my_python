numbers = [87, -8, 23, 1, 7, 35, 61]
numbers.sort()
print(numbers)

# 元のリストは並べ替えす、並べ替えた新しいリストを欲しい場合
numbers = [87, -8, 23, 1, 7, 35, 61]
numbers2 = sorted(numbers)
print(f"numbers={numbers}") # numbersは元の並びのまま
print(f"numbers2={numbers2}")

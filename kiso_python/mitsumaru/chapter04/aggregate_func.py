numbers = [5, 10, 7, 2, 1, 4, 9, 3, 8, 6]

print(f'合計: {sum(numbers)} 平均: {sum(numbers) / len(numbers)} 最大: {max(numbers)} 最小: {min(numbers)}')

total = 0
cnt = 0
saidai = numbers[0]
saisho = numbers[0]

for n in numbers:
    total += n
    cnt += 1
    if n > saidai:
        saidai = n
    if n < saisho:
        saisho = n

print(f'合計: {total} 平均: {total / cnt} 最大: {saidai} 最小: {saisho}')
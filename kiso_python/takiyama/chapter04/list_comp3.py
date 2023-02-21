dollars = [1, 5, 9.5, 100]
rate = 101

total_yen = sum([dollar * rate for dollar in dollars])
print(total_yen)

yens = []
for dollar in dollars:
    yens.append(dollar * rate)
    
total_yen = sum(yens)
print(total_yen)
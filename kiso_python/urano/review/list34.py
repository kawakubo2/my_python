list34 = [
    {'name': 'Yamada', 'salary': 25},
    {'name': 'Tanaka', 'salary': 38},
    {'name': 'Suzuki', 'salary': 18},
    {'name': 'Sato',   'salary': 28},
    {'name': 'Sasaki', 'salary': 32},
]

# 5名のsalaryの合計
salary_total = 0
for employee in list34:
    salary_total += employee['salary']
    
print(f"合計: {salary_total}")
print(f"平均: {salary_total/len(list34):.1f}")
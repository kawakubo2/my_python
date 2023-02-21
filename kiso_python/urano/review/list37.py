list37 = [
    {'部署': '開発', 'salary': 22},
    {'部署': '人事', 'salary': 25},
    {'部署': '開発', 'salary': 40},
    {'部署': '経理', 'salary': 28},
    {'部署': '開発', 'salary': 33},
    {'部署': '営業', 'salary': 35},
]

#
# 開発部のsalaryの合計
#

salary_total = 0

for employee in list37:
    if employee['部署'] == '開発':
        salary_total += employee['salary']

print(f"合計: {salary_total}")
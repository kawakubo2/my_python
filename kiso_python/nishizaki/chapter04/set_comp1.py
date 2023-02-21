lst = [100, 200, 100, 200, 300, 400, 90, 100, 50]
num = {num for num in lst if num > 100}
print(num)

members = [1001, 2013, 1240, 1001, 1200, 2013, 2056, 1300, 1240]

lastyear_members = {m for m in members if m < 2000}
print(lastyear_members)
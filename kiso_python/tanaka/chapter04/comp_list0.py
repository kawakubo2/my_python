s = "日月火水木金土"

weekdaylist = [w + "曜日" for w in s]
print(weekdaylist)

weekdaylist2 = []
for w in s:
    weekdaylist2.append(w + "曜日")
    
print(weekdaylist2)

numbers = [-2, 1, 5, 3, -5, 6, 8, 4]

print(sum([num for num in numbers if num > 0]))

positive_numbers = []
for num in numbers:
    if num > 0:
        positive_numbers.append(num)
print(sum(positive_numbers))

numbers2 = [num * num for num in numbers]
print(numbers2)

files = ['abc.py', 'bcd.java', 'cde.py', 'def.cpp', 'efg.py', 'fgh.c', 'ghi']
python_files = [file for file in files if file.endswith('.py')]
print(python_files)
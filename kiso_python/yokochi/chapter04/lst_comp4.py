import math

weekdays = [day + "曜日" for day in "日月火水木金土"]
print(weekdays)

numbers = [1, 5, 4, 2, 6, 7, 8]

circle_area_list = [r ** 2 * math.pi for r in numbers if r % 2 == 0]
print(circle_area_list)
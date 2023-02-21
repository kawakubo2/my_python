dollars = [1, 5, 9.5, 100]
rate = 126
yens = [dollar * rate for dollar in dollars]
print(yens)

weekdays = {"日": "Sunday", "月": "Monday", "火": "Tuesday", "水": "Wednesday",
            "木": "Thursday", "金": "Friday", "土": "Saturday"}

weekdayslist = [ ja + "(" + en + ")" for ja, en in weekdays.items()]
print(weekdayslist)

numbers = [10, 20, 30, 10, 20, 40, 80, 10]
numbers_set = {num for num in numbers}
numbers_set.add(70)
numbers_set.add(90)
print(numbers_set)

仕入担当 = {'山田太郎', '和田実', '内藤友美', '横山花子', '鈴木次郎', '星山裕子'}
売上担当 = {'田中一郎', '横山花子', '山本久美子', '内藤友美', '猫山五郎', '佐藤勝男'}

仕入担当兼売上担当 = 仕入担当 & 売上担当
print(仕入担当兼売上担当)

仕入担当専任 = 仕入担当 - 売上担当
print(仕入担当専任)

仕入担当売上担当 = 仕入担当 | 売上担当
print(仕入担当売上担当)
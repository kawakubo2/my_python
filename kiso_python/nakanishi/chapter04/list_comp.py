print("--- 内包表記を使用しない方法 ---")
lst = []
for num in range(0, 21, 2):
    lst.append(num ** 2)
print(lst)

print("--- 内包表記を使用する方法 ---")
lst2 = [num ** 2 for num in range(0, 21, 2)]
print(lst2)

numbers = [5, 4, -3, 1, 7, -5, 6]
positive_numbers = [num ** 2 for num in numbers if num > 0]
print(positive_numbers)

lst3 = []
for num in numbers:
    if num > 0:
        lst3.append(num ** 2)
print(lst3)        

langs = ['aaa.py', 'bbb.java', 'ccc.py', 'ddd.js', 'eee.cs', 'fff.py']
python_files = [lang.upper() for lang in langs if lang.endswith('.py')]
print(python_files)

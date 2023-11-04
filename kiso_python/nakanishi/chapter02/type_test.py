x = 1000
print(type(x))
x = "ABC"
if type(x) == int:
    print(x * 100)
print(type(x))
x = lambda x: x ** 2
print(type(x))

# 動的型付け言語・・・Python, JavaScript, Ruby
# 静的型付け言語・・・C, C++, Java, C#
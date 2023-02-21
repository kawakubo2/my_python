def my_gen1(str):
    for c in str.upper():
        yield c

gen = my_gen1("Hello")
while True:
    try:
        print(next(gen))
    except StopIteration:
        break

# 下記のfor文は上記のように内部では動いている
# 下記は上記の糖衣構文(シンタックスシュガー)と呼ぶ    
gen = my_gen1("Python")
for c in gen:
    print(c)
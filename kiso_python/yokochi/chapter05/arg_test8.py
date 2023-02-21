def func(**dic):
    print(dic)

func(name='田中一郎', num=1)
func(name='山田太郎', age=59, num=2, point=60)

# func(arg, *argv, **dic)
# print(*argv, **dic)

def add(x, y):
    x + y
def sub(x, y):
    x - y

def func(x, y, f):
    return f(x, y)

print(func(10, 20, add))
print(func(10, 20, sub))
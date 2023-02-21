def func(**dic):
    print(dic)

func(name='田中一郎', num=1)
func(name='山田太郎', age=59, num=2, point=60)

def func2(arg, *argv, **dic):
    print(arg)
    print(argv)
    print(dic)


func2('abc', 1, 2, 3, name='山田太郎', age=35)

def doll_to_yen(doll, rate=100):
    return doll * rate

print(doll_to_yen(rate=105, doll=200))
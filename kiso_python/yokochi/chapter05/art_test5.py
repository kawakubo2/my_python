def func(arg1, *arg2):
    print(arg1, arg2)

func(1, 2, 3, 4)
func('Hello', 'Python', 2015, 3, 5)

def func2(*arg1, arg2):
    print(arg1, arg2)
func2(1, 2, 3, arg2 = 4)
func2('Hello', 'Python', 2015, 3, arg2 = 5)
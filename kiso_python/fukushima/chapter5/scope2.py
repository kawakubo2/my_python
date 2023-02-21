# -*- coding: utf-8 -*-

value2 = 100

def scope_test2():
    value2 = 1
    print('ローカル変数value2=', value2)

scope_test2()
print(value2)


def func2(arg, *argv, **karg):
    print(arg)
    print(argv)
    print(karg)
    

def func2(*argv, arg , **karg):
    print(arg)
    print(argv)
    print(karg)



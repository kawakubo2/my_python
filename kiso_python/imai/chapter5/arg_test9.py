# -*- coding: utf-8 -*-

def func(arg, **dic):
    print(arg)
    print(dic)
    
    
func(123, name="田中", age=38, bmi=25)

def func2(arg, *argv, **dic):
    print(arg)
    print(argv)
    print(dic)
    
func2(123, 'A', 'B', 'C', name='Yamada', age=38, birthdate='1989-12-23')
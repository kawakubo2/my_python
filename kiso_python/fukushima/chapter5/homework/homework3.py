# -*- coding: utf-8 -*-
#宿題3（8/22）higher order finction を用いた処理の作成

def inp_data(arg1):
    if arg1 == 'int':
        msg = '整数を入力してください：'
    elif arg1 == 'float':
        msg = '実数を入力してください：'
    else:
        msg = '何か入力してください：'
    
    temp = input(msg)
    return temp

def cnv_inp_data(func,arg1):
    temp = func(arg1)
    try:
        if arg1 == 'int':
            return int(temp)
        elif arg1 == 'float':
            return float(temp)
        else:
            return temp
    except ValueError:
        return '入力値と型の関係が誤っています'

print(cnv_inp_data(inp_data,'int'))
print(cnv_inp_data(inp_data,'float'))
print(cnv_inp_data(inp_data,''))

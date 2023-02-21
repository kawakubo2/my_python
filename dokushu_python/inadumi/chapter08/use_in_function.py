data1 = 100

def func1():
    print(data1) # 代入していない変数はグローバル変数とみなされる

def func2():
    data1 = 10000
    print(data1) # 関数内で初期化するとグローバル変数ではなくローカル変数とみなされる

def func3():
    global data1
    data1 = 10000
    print(data1) # 関数内で初期化するとグローバル変数ではなくローカル変数とみなされる

func1()
func2()
print(f"data1={data1}")
func3()
print(f"data1={data1}")
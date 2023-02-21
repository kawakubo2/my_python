value1 = 1
def scope_test1():
    print(value1)
    
scope_test1()

value3 = 1
def scope_test3():
    value3 = 100 # 変数に値を代入するとローカル変数となる
    print(f"関数内部のvalue3: {value3}")
    
scope_test3()
print(f"グローバルvalue3: {value3}")

value4 = 1
def scope_test4():
    global value4
    value4 = 100 # globalを宣言しているので、変数に値を代入しても
                 # ローカル変数にはならない
    print(f"関数内部value4: {value4}")
    
scope_test4()
print(f"グローバルvalue4: {value4}")
value1 = 1
def scope_test1():
    global value1
    value1 = 100
    print(f"関数内部: {value1}")
    
scope_test1()
print(f"グローバル: {value1}")
value1 = 1

def scope_test1():
    global value1
    value1 = 10
    print(value1)

scope_test1()
print(value1)
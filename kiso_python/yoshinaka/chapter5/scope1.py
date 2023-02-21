value1 = 1
def scope_test1():
    value1 = 100
    print('関数内のvalue1:', value1)

scope_test1()
print('グローバル変数value1:', value1)
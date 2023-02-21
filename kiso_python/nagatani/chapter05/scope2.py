value2 = 100

def scope_test2():
    value2 = 10
    print(f"scope_test2内のvalue2={value2}")

scope_test2()
print(value2)
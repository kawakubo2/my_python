value2 = 1
def scope_test2():
    global value2
    value2 = 100
    print(f"scope_test2: {value2}")

scope_test2()

print(f"global scope: {value2}")
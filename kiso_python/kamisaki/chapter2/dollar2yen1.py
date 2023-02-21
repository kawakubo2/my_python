a = 10
a = "ABC"
a = True

print(type(a))

if type(a) == bool:
    print('bool型です')

n = 9 / 4
m = 9 // 4

print(n)
print(m)

x = 100_000_000 * 1_000_000_000

s = "He's teacher."
print(s)
s = "He's\n \"GREAT\"\t\t\t teacher."
print(s)
print("Caf\u00E9")
print("\u0417\u0434\u0440\u0430\u0432\u0435\u0439\u0442\u0435")

x = 123456
x = 1.23e5 # 1.23 * 100000
print(x)
print(1.23e12)
print(1.23e-9)

print(float("1.23e12"))
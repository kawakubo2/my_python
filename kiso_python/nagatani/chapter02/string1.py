name = '山田太郎'

print(name[0])
print(name[1])
print(name[2])
print(name[3])

for c in name:
    print(f'{c}')

for i in range(len(name)):
    print(name[i])

t1 = ('aaa', 'bbb', 'ccc', 'ddd')
print(t1[0])
print(t1[1])
print(t1[2])
print(t1[3])

for c in t1:
    print(c)
    
s1 = 'abc'
print(id(s1))
print(id('abc'))
print(s1)
s1 = 'xyz'
print(s1)


# -*- coding: utf-8 -*-

colors1 = ['yellow', 'red', 'green']
colors2 = ['黄色', '赤', '緑']

for en, ja in zip(colors1, colors2):
    print("{:6s}:{}".format(en, ja))
    
for index in range(len(colors1)):
    print(colors1[index] + ':' + colors2[index])
    
x = 10
y = 3
print("{:3d} / {:3d} = {:.2f}".format(x, y, x / y))
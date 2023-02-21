# -*- coding: utf-8 -*-

names = ['山田', '井上', '太田', '田中']
names[1] = '江藤'
try:
    names[9] = '加藤'
except IndexError:
    print('指定したインデクスは存在しません')
    
print(names)

names.insert(1, '鈴木')

print(names)

names.append('佐々木')

print(names)

yamada = [50, 78, 92]
inoue  = [72, 51, 61]
ohta   = [70, 89, 62]

class_score = []
class_score.append(yamada)
class_score.append(inoue)
class_score.append(ohta)

print(class_score)

class_total = 0
for kojin_score in class_score:
    kojin_total = 0
    for score in kojin_score:
        print('{:4d}'.format(score), end='')
        kojin_total += score
    print('{:5d}'.format(kojin_total))
    class_total += kojin_total
print('{:12s}{:5d}'.format(' ', class_total))
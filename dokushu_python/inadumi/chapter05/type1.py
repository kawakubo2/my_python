s = 'the c++ programming language'
print(s.title())
print(s.capitalize())

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age =  age
    
    def bark(self):
        print(self.name + 'はワンワンなく')

    def intro(self):
        print('{}は{}歳です。'.format(self.name, self.age))

dog = Dog('ポチ', 3) # コンストラクタ
dog.bark()
dog.intro()

data = [25, 3, 49, 67, 14]
for n in sorted(data, reverse=True):
    print(n)

print(data)
data.sort(reverse=True)
print(data)

print(dog.name)
print(dog.age)

import math
radius = 5

print(math.pow(radius, 2) * math.pi)

print("ぼくは\t\t\t\t\tPythonを\nを勉強している")

print("\t".isspace())

lang = 'Java\b'

print("\2078")

print(lang.strip('\b') == 'Java')


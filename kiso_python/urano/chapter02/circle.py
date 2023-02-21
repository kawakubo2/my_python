# circle.py

from math import pow, pi

# radius(半径)
radius = float(input('半径を入力してください: '))
print('半径が' + str(radius) + 'の円の面積は' + str(pow(radius, 2) * pi))
print('半径が' + str(radius) + 'の球の体積は' + str(4 / 3.0 * pi * pow(radius, 3)))
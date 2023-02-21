# circle.py
import math

radius = float(input('半径: '))
print('半径が' + str(radius) + 'の円の面積は' + str(math.pow(radius, 2) * math.pi))
# trapezoid.py
import sys

upperbases = [ 5, 4, 3, 6]
lowerbases = [ 5, 6, 7, 4]
heights    = [ 5, 5, 5, 5]

if not (len(upperbases) == len(lowerbases) == len(heights)):
    print('上底、下底、高さのリストの要素数が一致しません。')
    sys.exit()

trapezoid_areas = []
for upperbase, lowerbase, height in zip(upperbases, lowerbases, heights):
    trapezoid_areas.append((upperbase + lowerbase) * height / 2)

print(trapezoid_areas)
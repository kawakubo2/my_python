# -*- coding: utf-8 -*-

import math

numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

circle_areas = [r ** 2 * math.pi for r in numbers if r > 0 and r % 2 == 0]

print(circle_areas)
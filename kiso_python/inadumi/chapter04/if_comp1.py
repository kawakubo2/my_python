# -*- coding: utf-8 -*-

nums1 = [1, 3, 7, 10, 9, 15, 20, 30]
nums2 = [n for n in nums1 if n % 3 == 0]
print(nums2)

import math
circle_areas = [r ** 2 * math.pi for r in nums1 if r % 2 == 0]
print(circle_areas)
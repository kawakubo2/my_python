# -*- coding: utf-8 -*-

# =============================================================================
# upper_base = float(input('上底 : '))
# lower_base = float(input('下底 : '))
# height     = float(input('高さ : '))
# 
# print('上底が{:.2f}cm、下底が{:.2f}cm、高さが{:.2f}cmの台形の面積は{:.2f}平方cmです。'\
#       .format(upper_base, lower_base, height,\
#               (upper_base + lower_base) * height / 2))
# =============================================================================

trapezoids = [
        (2.3253, 4.235423, 7.352),
        (10.7273, 9.18938, 12.5829),
        (3.84924, 1.891734, 2.8983)
        ]

for trapezoid in trapezoids:
    upper_base, lower_base, height = trapezoid
    print('上底が{:6.2f}cm、下底が{:6.2f}cm、高さが{:6.2f}cmの台形の面積は{:7.2f}平方cmです。'\
      .format(upper_base, lower_base, height,\
              (upper_base + lower_base) * height / 2))
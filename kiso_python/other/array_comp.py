# リストの内包表記
import math
numbers = [12, 5, 2, 7, -3, 10, 4]
circle_area_total = sum([r ** 2 * math.pi for r in numbers if r > 0 and r % 2 == 0])
print(f"合計: {circle_area_total}")

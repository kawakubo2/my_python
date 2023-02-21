import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 面積を計算
    def get_area(self):
        return self.width * self.height

    # 対角線の長さを計算
    def get_diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

rectangles = [Rectangle(3, 4), Rectangle(6, 8), Rectangle(10, 20), Rectangle(12.3, 8.7)]

total_area = 0
for r in rectangles:
    print(f"面積: {r.get_area():.2f} 対角線の長さ: {r.get_diagonal():.2f}")
    total_area += r.get_area()

print(f"合計面積: {total_area:.2f}")
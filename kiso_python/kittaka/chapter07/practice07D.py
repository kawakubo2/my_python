import math
from practice07C import Circle

class NewCircle(Circle):
    def menseki(self):
        return self.radius ** 2 * math.pi

if __name__ == '__main__':
    c1 = NewCircle(10, "black")
    print(f"半径: {c1.radius}, 色: {c1.color}, 面積: {c1.menseki():.2f}")
# rectangle.py (長方形クラス)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        """
        面積を求めるメソッド
        """
        return self.width * self.height

    def diagonal(self):
        """
        対角線の長さを求めるメソッド
        """
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def perimeter(self):
        """
        外周の長さを求めるメソッド
        """
        return (self.width + self.height) * 2
    
if __name__ == '__main__':
    r1 = Rectangle(4, 3)
    r2 = Rectangle(6, 8)

    print(f"r1: 面積: {r1.area()} 対角線: {r1.diagonal()} 外周: {r1.perimeter()}")
    print(f"r2: 面積: {r2.area()} 対角線: {r2.diagonal()} 外周: {r2.perimeter()}")
    
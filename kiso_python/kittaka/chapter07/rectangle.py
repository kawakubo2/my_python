import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    # 面積を返すメソッド
    def area(self):
        """面積を返すメソッド

        Returns:
            float : 面積
        """
        return self.width * self.height
    
    # 外周を返すメソッド
    def perimeter(self):
        return (self.width + self.height) * 2
    
    # 対角線の長さを返すメソッド
    def diagonal(self):
        return math.hypot(self.width, self.height)

rec1 = Rectangle(3, 4)
rec2 = Rectangle(6, 8)


print(f"幅: {rec1.width} 高さ: {rec1.height} 面積: {rec1.area()} 外周: {rec1.perimeter()} 対角線: {rec1.diagonal()}")
print(f"幅: {rec2.width} 高さ: {rec2.height} 面積: {rec2.area()} 外周: {rec2.perimeter()} 対角線: {rec2.diagonal()}")
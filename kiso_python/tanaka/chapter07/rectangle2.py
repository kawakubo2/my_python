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
    print("長方形を作ります")
    width = float(input("幅を入力してください: "))
    height = float(input("高さを入力してください: "))
    n = int(input('求めるものは? 1.面積 2.対角線 3.外周 : '))
    
    rec = Rectangle(width, height)
    
    if n == 1:
        print(f"面積は{rec.area()}")
    elif n == 2:
        print(f"対角線は{rec.diagonal()}")
    elif n == 3:
        print(f"外周は{rec.perimeter()}")
    else:
        print("1～3を選択してください")
    
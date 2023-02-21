import math

class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_diagonal(self):
        return math.hypot(self.width, self.height)
    def get_perimeter(self):
        return (self.width + self.height) * 2
    def __str__(self):
        return f"Rectangle class: width={self.width} height={self.height}"

if __name__ == '__main__':
    
    def print_areas(*rects):
        for r in rects:
            print(f"{r.get_area()} ", end='')
        print()

    r1 = Rectangle(8, 5)
    r2 = Rectangle(10, 6)
    r3 = Rectangle(7, 5)
    r4 = Rectangle(9, 6)
   
    print_areas(r1, r2, r3, r4)
    r1.width = 12
    r1.height = 15
    r3.height = 10
    r4.width = 18 
    print_areas(r1, r2, r3, r4)
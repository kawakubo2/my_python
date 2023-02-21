class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        
c1 = Circle(10, "black")
print(f"半径: {c1.radius}, 色: {c1.color}")
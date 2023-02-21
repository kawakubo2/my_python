class Circle():
    def __init__(self, radius, color="white"):
        self.radius = radius
        self.color = color

if __name__ == "__main__":
    c1 = Circle(10, "black")
    print(f"半径: {c1.radius}, 色: {c1.color}")
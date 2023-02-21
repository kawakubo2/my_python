class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

if __name__ == '__main__':
    c1 = Circle(10, 'black')
    print('半径: {} 色: {}'.format(c1.radius, c1.color))
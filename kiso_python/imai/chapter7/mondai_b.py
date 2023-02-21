class Circle:
    def __init__(self, radius, color='white'):
        self.radius = radius
        self.color = color

c1 = Circle(10, 'black')

print('半径: {}, 色: {}'.format(c1.radius, c1.color))
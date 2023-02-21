import math
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __call__(self, o_x, o_y):
        # return math.hypot(o_x - self.x, o_y - self.y)
        # return math.sqrt(math.pow(o_x - self.x, 2) + math.pow(o_y - self.y, 2))
        return ((o_x - self.x) ** 2 + (o_y - self.y) ** 2) ** 0.5
       
if __name__ == '__main__':
    c = Coordinate(10, 20) 
    print(c(5, 15))

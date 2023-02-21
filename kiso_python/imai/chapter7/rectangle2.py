from figure import Figure

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def __str__(self):
        return "Rectangle class: width = {}, height = {}".format(self.width, self.height)
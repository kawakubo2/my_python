from figure import Figure

class Triangle(Figure):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def getArea(self):
        return self.base * self.height / 2

    def __str__(self):
        return "Triangle class: base = {}, height = {}".format(self.base, self.height)
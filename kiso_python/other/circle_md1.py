class Circle:
	def __init__(self, radius, color):
		self.__radius = radius
		self.__color = color
	
	def get_radius(self):
		return self.__radius
	
	def get_color(self):
		return self.__color
	
	radius = property(get_radius)
	color = property(get_color)

import math

class NewCircle(Circle):
	def menseki(self):
		return math.pow(self.radius, 2) * math.pi

if __name__ == "__main__":
	c1 = Circle(10, "black")
	print("半径: {}, 色: {}".format(c1.radius, c1.color))
	c2 = NewCircle(5, "yellow")
	print("半径: {}, 色: {}, 面積: {:.2f}".format(c2.radius, c2.color, c2.menseki()))


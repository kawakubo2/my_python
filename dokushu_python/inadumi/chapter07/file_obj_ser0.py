import pickle
import os
from rectangle import Rectangle

rectangles = [
    Rectangle(10, 20),
    Rectangle(20, 30),
    Rectangle(30, 40)
]


with open("./dokushu_python/inadumi/chapter07/rectangles.bin", "wb") as file:
    pickle.dump(rectangles, file)
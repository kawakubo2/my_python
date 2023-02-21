# coding: utf-8

class Dasai:
    def __init__(self, animal):
        self.animal = animal

    def ls(self):
        print("吾輩は" + self.animal + "である")

dasai1 = Dasai("猫")
dasai1.ls()


# -*- coding: utf-8 -*-
import random

class Dice:
    faces = set(range(4, 101, 2))
    def __init__(self, material, form, face=6):
        if face not in Dice.faces:
            raise ValueError('存在しない面体')
        self.material = material
        self.form = form
        self.face = face
        
    def roll(self):
        return random.randint(1, self.face)

try:  
    d1 = Dice('metal', 'abc', 100)
    for n in range(100):
        print(d1.roll())
except ValueError as er:
    print(er)
    

    
    
        
    
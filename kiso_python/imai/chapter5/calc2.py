# -*- coding: utf-8 -*-

class MyCalc:
    
    def __init__(self):
        self.__total = 0
        
    def add(self, n):
        self.__total += n
        
    def sub(self, n):
        self.__total -= n

    def mul(self, n):
        self.__total *= n

    def div(self, n):
        self.__total /= n
        
    def getTotal(self):
        return self.__total
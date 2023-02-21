# -*- coding: utf-8 -*-

class Calculator:
    def __init__(self):
        self.total = 0
        
    def add(self, num):
        self.total += num
        
    def sub(self, num):
        self.total -= num
        
    def mul(self, num):
        self.total *= num
        
    def div(self, num):
        self.total /= num
        
    def clear(self):
        self.total = 0
        
    def get_total(self):
        return self.total
    
class CalculatorWrapper:
    operators = ['+', '-', '*', '/', '=']
    def __init__(self, cal):
        self.cal = cal
        self.current_operator
        self.operator_mod = False
        self.char_list = []
    def run(self):
        while(True):
            if self.operator_mode:
                while(True):
                    self.current_operator = input('演算子(+-*/=):')
                    if self.current_operator in CalculatorWrapper.operators:
                        self.operator_mode = False
                        self.char_list = []
                        break
                    else:
                        print('演算子に誤りがあります')
            else:
                while(True):
                    try:
                        num = float(input('数値:'))
                        break
                    except:
                        print('数値形式に誤りがあります')
                if self.current_operator == '+':
                    self.cal.add(num)
                elif self.current_operator == '-':
                    self.cal.sub(num)
                elif self.current_operator == '*':
                    self.cal.mul(num)
                elif self.current_operator == '/':
                    self.cal.div(num)
                elif self.current_operator == '=':
                    print('total={}'.format(self.cal.get_total()))
                self.operator_mode = True
                    
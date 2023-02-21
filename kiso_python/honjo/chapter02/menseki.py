# -*- coding: utf-8 -*-

import math

hankei = float(input("半径を入力してください : "))

menseki = math.pi * math.pow(hankei, 2)
print("半径が" + str(hankei) + "の面積は" + str(menseki) + "です")

import numpy as np

numbers = np.arange(1,10)
print(numbers)
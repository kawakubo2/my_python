# -*- coding: utf-8 -*-
import math


inches = [9, 5.5, 6, 4, 5, 6.5, 10]
formatted_cms = ["{:.1f}".format(n * 2.54) for n in inches]
print(formatted_cms)
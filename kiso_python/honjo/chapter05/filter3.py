# -*- coding: utf-8 -*-

inches = [9, 5.5, 6, 4, 6.5, 10]

cms = [inch * 2.54 for inch in inches if inch > 5]

print(cms) 

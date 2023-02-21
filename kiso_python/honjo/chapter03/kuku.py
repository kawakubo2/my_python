# -*- coding: utf-8 -*-

for i in range(1, 100):
    for j in range(1, 100):
        if i * j > 300:
            break;
        print(str(i * j) + "\t", end = "")
    print("")
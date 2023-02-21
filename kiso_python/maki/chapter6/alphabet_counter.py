# -*- coding: utf-8 -*-

# alphabet_counter.py

dic = {}

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

for c in alphabet:
    dic[c] = 0

with open("The_Return_of_the_Native_pg122.txt", "r", encoding="utf-8") as f:
    for line in f:
        for c in line:
            if c in dic:
                dic[c] += 1

for alpha, cnt in dic.items():
    print("{}:{}".format(alpha, cnt))
        
    
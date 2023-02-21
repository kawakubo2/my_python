# -*- coding: utf-8 -*-

word1 = {"空", "海", "川", "地球"}
word2 = {"山", "海", "空", "空気"}

print(word1 | word2)
print(word1 & word2)
print(word1 - word2)
print(word1 ^ word2)

w3 = set()
for w1 in word1:
    if w1 in word2:
        w3.add(w1)
print(w3)
        

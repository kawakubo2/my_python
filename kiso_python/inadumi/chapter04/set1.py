# -*- coding: utf-8 -*-

words1 = {'空','海','川','地球'}
words2 = {'山','海','空','空気'}

print(words1 | words2)
print(words1 & words2)
print(words1 - words2)
print(words1 ^ words2)
#
print((words1 - words2) | (words2 - words1))
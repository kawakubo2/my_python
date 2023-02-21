# -*- coding: utf-8 -*-

words1 = {"空", "海", "川", "地球"}
words2 = {"山", "海", "空", "空気"}

# 和集合(union)

words3 = words1 | words2
print(words3)

# 積集合

words4 = words1 & words2
print(words4)

# 差集合

words5 = words1 - words2
print(words5)

# 対称差集合

words6 = words1 ^ words2
print(words6)
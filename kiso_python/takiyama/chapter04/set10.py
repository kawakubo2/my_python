words1 = {"空", "海", "川", "地球"}
words2 = {"山", "海", "空", "空気"}

print(words1 | words2) # 和集合
print(words1 & words2) # 積集合
print(words1 - words2) # 差集合
print(words1 ^ words2)
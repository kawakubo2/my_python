words1 = {"空", "海", "川", "地球"}
words2 = {"山", "海", "空", "空気"}

print(words1 | words2)
print(words1 & words2)
print(words1 - words2)
print(words1 ^ words2)

def intersect(set1, set2):
    result = set();
    for e in set1:
        if e in set2:
            result.add(e)
    return result

def minus(set1, set2):
    result = set();
    for e in set1:
        if e not in set2:
            result.add(e)
    return result

print(intersect(words1, words2))
print(minus(words1, words2))

print(words1.union(words2))          # |
print(words1.intersection(words2))   # &
print(words1.difference(words2))     # -
print(words1.symmetric_difference(words2)) # ^

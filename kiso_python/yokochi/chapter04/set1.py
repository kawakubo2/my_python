set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {1, 2, 4, 8, 16, 32, 64, 128}

print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set2 - set1)

def union(s1, s2):
    s3 = set()
    for e1 in s1:
        s3.add(e1)
    for e2 in s2:
        s3.add(e2)
    return s3

def intersection(s1, s2):
    s3 = set()
    for e in s1:
        if e in s2:
            s3.add(e)
    return s3

def exception(s1, s2):
    s3 = set()
    for e in s1:
        if e not in s2:
            s3.add(e)
    return s3

print(union(set1, set2))
print(intersection(set1, set2))
print(exception(set1, set2))
print(exception(set2, set1))
def issubstring(s1, s2, ignore_case = True):
    if ignore_case:
        s1 = s1.upper()
        s2 = s2.upper()
    return s2 in s1

in1 = input("対象文字列: ")
in2 = input("検索文字列: ")

print(issubstring(in1, in2))
print(issubstring(in1, in2, False))
s1 = {1, 2, 3, 4, 5, 6}
s2 = {1, 2, 4, 8, 16}
s9 = {2, 4, 6, 8}

print('===< intersection >===\n')
print('---< s3 = s1 & s2 >---')
s3 = s1 & s2
print('s1 =', s1)
print('s2 =', s2)
print('s3 =', s3)

print('---< s3 = s1.intersection(s2) >---')
s3 = s1.intersection(s2)
print('s1 =', s1)
print('s2 =', s2)
print('s3 =', s3)

print('---< s3 = s1.intersection(s2, s9) >---')
s3 = s1.intersection(s2, s9)
print('s1 =', s1)
print('s2 =', s2)
print('s9 =', s9)
print('s3 =', s3)

print('---< s1 &= s2 >---')
s1 &= s2
print('s1 =', s1)
print('s2 =', s2)
print('s3 =', s3)

print('---< s1 = {1, 2, 3, 4, 5, 6} >---')
s1 = {1, 2, 3, 4, 5, 6}
print('--- s1.intersection_update(s2, s9) >---')
s1.intersection_update(s2, s9)
print('s1 =', s1)
print('s2 =', s2)
print('s9 =', s9)

print('\n===< union >===\n')

print('---< s1 = {1, 2, 3, 4, 5, 6} >---')
s1 = {1, 2, 3, 4, 5, 6}
print('---< s3 = s1 | s2 >---')
s3 = s1 | s2
print('s1 =', s1)
print('s2 =', s2)
print('s3 =', s3)

print('--- s3 = s1.union(s2) >---')
s3 = s1.union(s2)
print('s1 =', s1)
print('s2 =', s2)
print('s3 =', s3)

print('---< s1 |= s2 >---')
s1 |= s2
print('s1 =', s1)
print('s2 =', s2)

print('---< s1 = {1, 2, 3, 4, 5, 6} >---')
s1 = {1, 2, 3, 4, 5, 6}
print('---< s1.update(s2, s9) >---')
s1.update(s2, s9)
print('s1 =', s1)
print('s2 =', s2)
print('s9 =', s9)

print('\n===< difference >===\n')

print('---< s1 = {1, 2, 3, 4, 5, 6} >---')
s1 = {1, 2, 3, 4, 5, 6}
print('---< s3 = s1 - s2 >---')
s3 = s1 - s2
print('s1 =', s1)
print('s2 =', s2)
print('s3 =', s3)

print('---< s3 = s1.difference(s2, s9) >---')
s3 = s1.difference(s2, s9)
print('s1 =', s1)
print('s2 =', s2)
print('s9 =', s9)
print('s3 =', s3)

print('---< s1 -= s2 >---')
s1 -= s2
print('s1 =', s1)
print('s2 =', s2)

print('---< s1 = {1, 2, 3, 4, 5, 6} >---')
s1 = {1, 2, 3, 4, 5, 6}
print('---< s1.difference_update(s2, s9) >---')
s1.difference_update(s2, s9)
print('s1 =', s1)
print('s2 =', s2)
print('s9 =', s9)

print('---< s1 = {1, 2, 3, 4, 5, 6} >---')
s1 = {1, 2, 3, 4, 5, 6}
print('---< s3 = s1.symmetric_difference(s2) >---')
s3 = s1.symmetric_difference(s2)
print('s1 =', s1)
print('s2 =', s2)
print('s3 =', s3)

print('===< symmetric differecnce >===')
print('---< s3 = s1 ^ s2 >---')
s3 = s1 ^ s2
print('s1 =', s1)
print('s2 =', s2)
print('s3 =', s3)

print('---< s1 ^= s2 >---')
s1 ^= s2 
print('s1 =', s1)
print('s2 =', s2)

print('---< s1 = {1, 2, 3, 4, 5, 6} >---')
s1 = {1, 2, 3, 4, 5, 6}
print('---< s1.symmetric_difference_update(s2) >---')
s1.symmetric_difference_update(s2)
print('s1 =', s1)
print('s2 =', s2)

print('\n===< disjoint ===\n')
print('---< s4.isdisjoint(s5) >---')
s4 = {1, 3, 5, 7, 9}
s5 = {2, 4, 6, 8, 10}
print('s4 =', s4)
print('s5 =', s5)
print('s4.isdisjoint(s5) =>', s4.isdisjoint(s5))
print('s5 =', s5)

print('\n===< contains ===\n')
n1 = 5
n2 = 6
print('n1 =', n1)
print('n2 =', n2)
print('---< n1 in s4 >---')
print('n1 in s4 =>', n1 in s4)
print('---< n2 in s4 >---')
print('n2 in s4 =>', n2 in s4)

print('\n===< subset >===\n')
s6 = {2, 4, 6, 8, 10}
print('s6 =', s6)
print('s5 <= s6 =>', s5 <= s6)

print('\n===< proper subset >===\n')
s0 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print('s0 =', s0)
print('s4 < s0 =>', s4 < s0)
print('s5 < s0 =>', s5 < s0)

print('\n===< superset >===\n')
s6 = {2, 4, 6, 8, 10}
print('s6 =', s6)
print('s5 >= s6 =>', s5 >= s6)

print('\n===< proper superset >===\n')
print('s0 =', s0)
print('s0 > s4 =>', s0 > s4)
print('s0 > s5 =>', s0 > s5)
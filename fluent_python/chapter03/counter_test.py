import collections

ct = collections.Counter('Tomoharu Kawakubo')
ct.update('charlie Sato')
print(ct)

ct2 = collections.Counter(['Java', 'Python', 'C++', 'C', 'Java', 'Ruby', 'JavaScript', 'Java', 'Python'])
print(ct2)
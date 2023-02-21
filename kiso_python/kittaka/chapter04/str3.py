s = "0123456"
print(s[1:5])
print(s[:4], s[4:])

s2 = "abcdefghijklmnopqrstuvwxyz"

step = 5
pos = 0
while True:
    if pos + step >= len(s2):
        print(s2[pos:len(s2)])
        break
    print(s2[pos: pos + step])
    pos += step
c1 = ["dog", "blue", "yellow", "dog", "red", "white", "dog"]
word = "dog"
while word in c1:
    c1.remove(word)
print(c1)

c2 = ["dog", "blue", "yellow", "dog", "red", "white", "dog"]
c3 = [ c for c in c2 if c != word]
print(c3)
import random
f = open("meigen2.txt", "r", encoding="utf-8")
lines = f.readlines()

index = random.randrange(len(lines) / 2)
en_meigen = lines[index * 2]
ja_meigen = lines[index * 2 + 1]
print(en_meigen.rstrip("\n"))
print(ja_meigen.rstrip("\n"))
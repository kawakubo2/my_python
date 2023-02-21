s = "123,456 ,  789"
temp = s.split(",")
lst = [c.strip() for c in temp]
for e in lst:
    print(f"|{e}|")
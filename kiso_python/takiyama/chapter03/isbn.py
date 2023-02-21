isbn = "9784798163642"
cd = 4
total = 0
for i, c in enumerate(isbn):
    if i % 2 == 0:
        total += int(c)
    else:
        total += int(c) * 3
        
print(f"total={total}")
if total % 10 == 0:
    print('○')
else:
    print('×')
    
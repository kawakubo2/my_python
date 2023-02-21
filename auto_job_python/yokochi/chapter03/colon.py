import os, csv

base_dir = os.path.dirname(__file__)
source = os.path.join(base_dir, 'test')

with open(source, encoding='utf_8') as f:
    reader = csv.reader(f, delimiter=":")
    total = 0
    for line in reader:
        subtotal = 0
        for num in line:
            print(f"{num:4}", end="")
            subtotal += int(num)
        total += subtotal
        print(f"{subtotal:5}")
    print(f"{' ' * 16}{total:5}")

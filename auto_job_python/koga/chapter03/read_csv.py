import csv, pprint, os

with open(os.path.dirname(__file__) + '/items.csv', encoding='sjis') as f:
    text = f.read().strip()
    lines = text.split("\n")
    data = [v.split(',') for v in lines]
    pprint.pprint(data)

with open(os.path.dirname(__file__) + '/items.csv', encoding='sjis') as f:
    reader = csv.reader(f)
    data = [row for row in reader]
    pprint.pprint(data)
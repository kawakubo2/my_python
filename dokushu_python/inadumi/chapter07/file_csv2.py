import csv, os
with open(os.path.dirname(__file__) + '/data2.tsv', encoding='UTF-8') as file:
    for row in csv.reader(file, delimiter='\t'):
        for cell in row:
            print(cell)
        print('-------------')
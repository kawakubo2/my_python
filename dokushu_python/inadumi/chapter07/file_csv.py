import csv

with open('./dokushu_python/inadumi/chapter07/data0.tsv', encoding='UTF-8') as file:
    for row in csv.reader(file, delimiter='\t', quoting=csv.QUOTE_NONNUMERIC):
        print(f"種類:{row[0]:10}", end="")
        print(f"単価:{row[1]:4.0f}\t", end="")
        print(f"数量:{row[2]:3.0f}\t", end="")
        print(f"金額:{row[1]*row[2]:5.0f} ")
        print('-----------------------------------------------------------------')
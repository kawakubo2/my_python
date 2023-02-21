# -*- coding: utf-8 -*-

class HousekeepingBookItem:
    def __init__(self, kdate, himokumei, memo, income, outcome):
        self.kdate = kdate
        self.himokumei = himokumei
        self.memo = memo
        self.income = income
        self.outcome = outcome
        
class HousekeepingBook:
    def __init__(self, items):
        self.items = items
        
    def add_item(self, item):
        self.items.append(item)
        
    def print_items(self):
        for item in self.items:
            print('{} {} {} {} {}'.format(item.kdate, item.himokumei,\
                  item.memo, item.income, item.outcome))

    def get_items(self):
        return self.items
            
class HousekeepingReader:
    def __init__(self, filepath, encoding='utf_8'):
        self.filepath = filepath
        self.encoding = encoding
        
    def read_file(self):
        items = []
        with open(self.filepath, 'r', encoding=self.encoding) as f:
            for line in f:
                ary = line.rstrip('\n').split(',')
                items.append(HousekeepingBookItem(ary[0], ary[1], ary[2],\
                        int(ary[3]), int(ary[4])))
        return items
    
class HousekeepingWriter:
    def __init__(self, filepath, encoding='utf_8'):
        self.filepath = filepath
        self.encoding = encoding
    
    def write_file(self, items):
        with open(self.filepath, 'w', encoding=self.encoding) as f:
            for item in items:
                result = ''
                result += item.kdate + ','
                result += item.himokumei + ','
                result += item.memo + ','
                result += str(item.income) + ','
                result += str(item.outcome) + '\n'
                f.write(result)
                
# 初期処理        
hk_reader = HousekeepingReader('housekeeping.csv', 'utf_8')
items = hk_reader.read_file()
hk_book = HousekeepingBook(items)

while(True):
    print('1:追加 2:表示 9:終了', end='')
    sw = int(input(' > '))
    if sw == 1:
        kdate = input('日付 > ')
        himokumei = input('費目名 > ')
        memo = input('メモ > ')
        income = int(input('入金額 > '))
        outcome = int(input('出金額 > '))
        hk_book.add_item(HousekeepingBookItem(kdate, himokumei, memo, income, outcome))
    elif sw == 2:
        hk_book.print_items()
    else:
        break

hk_writer = HousekeepingWriter('housekeeping.csv', 'utf_8')
hk_writer.write_file(hk_book.get_items())

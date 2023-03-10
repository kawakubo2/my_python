import openpyxl as excel, json
import os

in_file = os.path.dirname(__file__) + '/matome.xlsx'
out_file = os.path.dirname(__file__) + '/matome.json'

def split_list():
    users = read_and_split(in_file)
    result = {}
    for name, rows in users.items():
        result[name] = calc_user(rows)
        print(name, result[name]['total'])
    with open(out_file, "wt") as fp:
        json.dump(result, fp)

def read_and_split(in_file):
    users = {}
    sheet = excel.load_workbook(in_file).active
    for row in sheet.iter_rows():
        values = [col.value for col in row]
        name = values[1]
        if name not in users:
            users[name] = []
        users[name].append(values)
    return users

def calc_user(rows):
    total = 0
    items = []
    for row in rows:
        date, _, item, cnt, price, _ = row
        date_s = date.strftime('%m/%d')
        items.append([date_s, item, cnt, price])
        total += cnt * price
    return{ 'items': items, 'total': total }

if __name__ == '__main__':
    split_list()
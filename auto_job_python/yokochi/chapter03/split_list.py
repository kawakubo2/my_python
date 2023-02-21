import openpyxl as excel
import os, json

in_file = 'matome.xlsx'
out_file = 'matome.json'

base_dir = os.path.dirname(__file__)

def split_list():
    # Excelソートのデータを顧客ごとに分ける
    users = read_and_split(os.path.join(base_dir, in_file))
    # 顧客ごとにでエータを集計する
    result = {}
    for name, rows in users.items():
        result[name] = calc_user(rows)
        print(name, result[name]['total'])
    # ファイルに結果を保存
    with open(os.path.join(base_dir, out_file), "wt") as fp:
        json.dump(result, fp)

# 入力ファイルを読み込んで顧客ごとに分割
def read_and_split(in_file):
    users = {}
    # ブックを開いてシートの全行を読む
    sheet = excel.load_workbook(os.path.join(base_dir, in_file)).active
    for row in sheet.iter_rows():
        # シートの1行を取り出してリストに変換
        values = [col.value for col in row]
        name = values[1] # 顧客名を取り出す
        if name not in users:
            users[name] = []
        # データを顧客ごとに分ける
        users[name].append(values)
    return users

def calc_user(rows):
    total = 0
    items = [] # 請求書の明細用
    # 集計処理を行う
    for row in rows:
        # 請求書に必要な項目だけ抽出して請求書明細の形式で追加
        date, _, item, cnt, price, _ = row
        date_s = date.strftime('%m/%d')
        items.append([date_s, item, cnt, price])
        # 合計金額を計算
        total += cnt * price
    # 集計処理を辞書形式で返す
    return { 'items': items, 'total': total }

if __name__ == '__main__':
    split_list()
    
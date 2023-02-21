import os, openpyxl as excel, csv, pprint;

base_dir = os.path.dirname(__file__)
in_file = os.path.join(base_dir, 'meibo.csv')
template_file = os.path.join(base_dir, 'card-template.xlsx')
save_file = os.path.join(base_dir, 'card-meibo.xlsx')

# CSVファイルを読み込む
def read_csv(fname):
    with open(fname, encoding='sjis') as f:
        reader = csv.reader(f)
        next(reader) # ヘッダを読み飛ばす
        return [v for v in reader]
    
# Excelブックを読み込む
book = excel.load_workbook(template_file)
# テンプレートのシートを得る
sheet_tpl = book['Sheet']
# CSVから顧客一覧を得て1人ずつ処理
def print_cards(lists, card_per_page = 10, rows = 5):
    for i, person in enumerate(read_csv(in_file)):
        # CSVの1行を変数に割り振る
        name, zipno, addr = person
        # 1枚のページにcard_per_page枚ずつ
        idx = i % card_per_page 
        if idx == 0:
            # テンプレートのシートをコピー
            sheet = book.copy_worksheet(sheet_tpl)
            sheet.title = f"Page{idx}"
        # 書き込むセル位置を決定
        row = 4 * (idx % rows) + 2
        col = 2 * (idx // rows) + 2
        # セルにデータを書きこむ
        sheet.cell(row=row+0, column=col, value=name)
        sheet.cell(row=row+1, column=col, value=zipno)
        sheet.cell(row=row+2, column=col, value=addr)
        
print_cards(read_csv(in_file), rows=3)

# テンプレートのシートを削除して保存
book.remove(sheet_tpl)
book.save(save_file)
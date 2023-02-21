import glob
import openpyxl as excel
import os

# 各部署から提出された売上ブックのフォルダ
target_dir = os.path.dirname(__file__) + '/salesbooks'
save_file = os.path.dirname(__file__) + '/matome.xlsx'

def read_files():
    # 売上一覧を書き込むブックを用意する
    book = excel.Workbook()
    main_sheet = book.active
    # ファイルを列挙して読み込む
    enumfiles(main_sheet)
    # 読み込んだデータを保存
    book.save(save_file)

def enumfiles(main_sheet):
    # Excelファイルの一覧を得る
    files = glob.glob(target_dir + "/*.xlsx")
    # 各Excelブックを次々と読んでいく
    print(files)
    for fname in files:
        read_book(main_sheet, fname)

# ブックを開いて中身を読む
def read_book(main_sheet, fname):
    print("read:", fname)
    # Excelブックを読み込む
    book = excel.load_workbook(fname, data_only=True)
    sheet = book.active
    # 売上データのある範囲を読み取る
    rows = sheet["A4": "F999"]
    for row in rows:
        # セルの値をリストとして得る
        values = [cell.value for cell in row]
        if values[0] is None: break
        print(values)
        # メインシートに値をコピー
        main_sheet.append(values)

# メインプログラムを実行
if __name__ == '__main__':
    read_files()
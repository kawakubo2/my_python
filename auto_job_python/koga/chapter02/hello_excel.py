import openpyxl as excel
import os
# 新規ワークブック
book = excel.Workbook()

# アクティブなワークシートを得る
sheet = book.active;

# A1セルに値を設定
sheet['A1'] = 'こんにちは';

book.save(os.path.dirname(__file__) + "/hello.xlsx")
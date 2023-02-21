import docx
import datetime
import os

template_file = os.path.dirname(__file__) + '/letter.docx'
save_file = os.path.dirname(__file__) + '/letter-suzuki.docx'
now = datetime.datetime.now()

# 置き換える文字列を指定
card = {
    '2021年10月10日': now.strftime('%Y年%m月%d日'),
    '●●●御中': 'ナイナビ出版御中',
    '■■■様': '鈴木様',
    '★★★の送付について': '契約書の送付について'
}

cstyle = {
    '★★★の送付について': True
}

# Wordフィアルを開く
doc = docx.Document(template_file)
for p in doc.paragraphs:
    # テキストを置き換え
    for k, v in card.items():
        if p.text.find(k) >= 0:
            p.text = p.text.replace(k, v)
            # 書式を設定するか?
            if k in cstyle:
                font = p.runs[0].font
                font.bold = True
                font.underline = True
                font.size = docx.shared.Pt(20)

# Wordファイルに保存
doc.save(save_file)
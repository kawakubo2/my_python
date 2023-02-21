import docx
import os

base_dir = os.path.dirname(__file__)
doc_filename = os.path.join(base_dir, 'letter.docx')

# 既存Wordファイルを読み込む
doc = docx.Document(doc_filename)

# 段落を順次表示
for p in doc.paragraphs:
    print(p.text)
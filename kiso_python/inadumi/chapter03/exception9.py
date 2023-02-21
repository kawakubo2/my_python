# -*- coding: utf-8 -*-

import random

def get_lesson_record():
    if random.randrange(10) > 7:
        print('受講記録の取得に失敗')
        raise ValueError()
    print('受講記録の取得に成功')

def create_pdf():
    if random.randrange(10) > 7:
        print('PDFファイルの作成に失敗')
        raise ValueError()
    print('PDFファイルの作成に成功')

def send_mail():
    if random.randrange(10) > 7:
        print('メールの送信に失敗')
        raise ValueError()
    print('メールの送信に成功')

try:
    get_lesson_record()
    create_pdf()
    send_mail()
except ValueError:
    pass
    

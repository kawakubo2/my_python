import random

class CannotGetRecord(Exception):
    def __init__(self, message):
        super().__init__(message)

class PDFError(Exception):
    def __init__(self, message):
        super().__init__(message)

class MailError(Exception):
    def __init__(self, message):
        super().__init__(message)

def get_lesson_records():
    if random.randrange(100) > 80:
        raise CannotGetRecord('受講記録の取得に失敗しました。')
    print('受講記録の取得に成功しました。')

def create_pdf():
    if random.randrange(100) > 80:
        raise PDFError('PDFの作成に失敗しました。')
    print('PDFの作成に成功しました。')

def send_mail():
    if random.randrange(100) > 80:
        raise MailError('メールの送信に失敗しました。')
    print('メールの送信に成功しました。')

try:
    get_lesson_records()
    create_pdf()
    send_mail()
except CannotGetRecord as e1:
    print(e1)
except PDFError as e2:
    print(e2)
except MailError as e3:
    print(e3)
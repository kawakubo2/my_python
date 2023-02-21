import random

class CannotGetRecordError(Exception):
    def __init__(self):
        pass
class PDFError(Exception):
    def __init__(self):
        pass

class MailSendError(Exception):
    def __init__(self):
        pass

def get_lesson_record():
    if random.randrange(100) >= 80:
        raise CannotGetRecordError()
    print('受講記録の取得に成功しました')
def create_pdf():
    if random.randrange(100) >= 80:
        raise PDFError()
    print('PDFファイルの作成に成功しました')
def send_mail():
    if random.randrange(100) >= 80:
        raise MailSendError()
    print('メールの送信に成功しました')

try:
    get_lesson_record()
    create_pdf()
    send_mail()
except CannotGetRecordError:
    print('受講記録の取得に失敗しました')
except PDFError:
    print('PDFファイルの作成に失敗しました')
except MailSendError:
    print('メールの送信に失敗しました')
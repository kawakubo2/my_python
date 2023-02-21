import random

class CannotGetException(Exception):
    def __init__(self, message):
        super().__init__(message)

class PDFException(Exception):
    def __init__(self, message):
        super().__init__(message)

class SendMailException(Exception):
    def __init__(self, message):
        super().__init__(message)



def get_lesson_records():
    """
    データベースから受講記録を取得
    """
    if random.randrange(100) > 80:
        raise CannotGetException("受講記録の取得に失敗しました。")
    print("受講記録の取得に成功しました。")

def create_pdf():
    """
    受講記録を元に請求書PDFを作成
    """
    if random.randrange(100) > 80:
        raise PDFException("PDFの作成に失敗しました。")
    print("PDFファイルの作成に成功しました。")

def send_mail():
    """
    請求書PDFを添付したメールを送信
    """
    if random.randrange(100) > 80:
        raise SendMailException("メールの送信に失敗しました。")
    print("メールの送信に成功しました。")

try:
    get_lesson_records()
    create_pdf()
    send_mail()
except CannotGetException as e1:
    print(e1)
except PDFException as e2:
    print(e2)
except SendMailException as e3:
    print(e3)

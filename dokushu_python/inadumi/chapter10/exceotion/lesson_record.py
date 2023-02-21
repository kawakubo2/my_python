import random

class LessonRecord:
    @staticmethod
    def getRecords():
        if random.randrange(100) > 80:
            raise CannotReadError("受講記録の読み込みに失敗しました。")
        print("受講記録の読み込みに成功しました。")

class CannotReadError(Exception):
    def __init__(self, message):
        super().__init__(message)

class PdfCreator:
    @staticmethod
    def create():
        if random.randrange(100) > 80:
            raise PDFCreateError("PDFファイルの作成に失敗しました。")
        print("PDFファイルの作成に成功しました。")

class PDFCreateError(Exception):
    def __init__(self, message):
        super().__init__(message)

class SendMail:
    @staticmethod
    def send():
        if random.randrange(100) > 80:
            raise SendMailError("メールの送信に失敗しました。")
        print("メールの送信に成功しました。")
            
class SendMailError(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    LessonRecord.getRecords()
    PdfCreator.create()
    SendMail.send()
except CannotReadError as e:
    print(e)
except PDFCreateError as e:
    print(e)
except SendMailError as e:
    print(e)
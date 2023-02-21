"""
1) 受講記録の取得
2) 請求書PDFの作成
3) 請求書を添付してメール送信
"""
import lessonrecord
import pdfcreator
import mymailsendor
try:
    lessonrecord1 = lessonrecord.LessonRecord()
    lessonrecord1.getStudentRecord()
    pdf = pdfcreator.PDFCreator()
    pdf.make()
    mail = mymailsendor.MyMailSendor()
    mail.send()
except lessonrecord.LessonRecordError as e:
    print(e)
except pdfcreator.PDFError as e:
    print(e)
except mymailsendor.MailSendError as e:
    print(e)

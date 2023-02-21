import smtplib, ssl, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import gmail_send
import my_gmail_account as gmail

msg = MIMEMultipart()
msg['Subject'] = 'ZIPファイルの添付テスト'
msg['From'] = gmail.account
msg['To'] = 'kawakubo@setagaya-pc.com'

txt = MIMEText('テキストでZIPファイルを送ります。')
msg.attach(txt)
# ZIPファイルを添付
zip_part = MIMEBase('application', 'zip')
filepath = os.path.join(os.path.dirname(__file__), 'test.zip')
with open(filepath, 'rb') as fp:
    zip_part.set_payload(fp.read())
encoders.encode_base64(zip_part)
zip_part.add_header('Content-Disposition',
                    'attachment', filename='test.zip')
msg.attach(zip_part)

gmail_send.send_gmail(msg)
print('ok')

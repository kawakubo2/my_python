import smtplib, ssl
from email.mime.text import MIMEText
import my_gmail_account as gmail
import gmail_send

msg = MIMEText('こんにちは。CCのテストでみんなに送っています！')
msg['Subject'] = 'CCのテスト'
msg['To'] = 'kawakubo@setagaya-pc.com'
msg['From'] = gmail.account
msg['Cc'] = gmail.account
msg.add_header('reply-to', 'tomo_kawakubo_0722@yahoo.co.jp')

gmail_send.send_gmail(msg)
print('ok')
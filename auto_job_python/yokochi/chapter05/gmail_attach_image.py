import smtplib, ssl, os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import gmail_send
import my_gmail_account as gmail

msg = MIMEMultipart()
msg['Subject'] = '猫の写真'
msg['From'] = gmail.account
msg['To'] = 'kawakubo@setagaya-pc.com'

text = MIMEText('本人はそうではないと思うけど。。。')
msg.attach(text)

image_file = os.path.join(os.path.dirname(__file__), 'cat2.jpg')
with open(image_file, 'rb') as fp:
    img = MIMEImage(fp.read())
    msg.attach(img)
    
gmail_send.send_gmail(msg)
print('ok')
    

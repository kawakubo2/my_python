import smtplib, ssl
from email.mime.text import MIMEText
import my_gmail_account
import gmail_send

html = '''
    <html>
        <head>
            <meta charset="UTF-8" />
            <style>
                body {
                    background: yellow;
                }
            </style>
        </head>
        <body>
            <h1>HTMLメールを送れます</h1>
            <p>仕事に役立つ格言</p>
            <ul>
                <li>もっとも重要な決定とは、何をするかではなく、何をしないかを決めることだ(スティーブジョブス)</li>
                <li>人から批判されることを恐れてはならない。それは成長の肥やしとなる(トーマスエジソン)</li>
                <li>良い名は多くの富に勝る(格言)</li>
            </ul>
        </body>
    </html>
'''

msg = gmail_send.make_mime_text(
    mail_to='kawakubo@setagaya-pc.com',
    subject='HTMLメールの送信テスト',
    body=html
)

gmail_send.send_gmail(msg)
print('ok')
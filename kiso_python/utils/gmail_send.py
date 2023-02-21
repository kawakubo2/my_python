import smtplib, ssl
from email.mime.text import MIMEText
import my_gmail_account as gmail

import gmail_send
import my_gmail_account as gmail

def send_test_email(body):
    msg = make_mime_text(
        mail_to='kawakubo@setagaya-pc.com',
        subject='メールの送信',
        body=body
    )
    send_gmail(msg)
    
def make_mime_text(mail_to, subject, body):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['To'] = mail_to
    msg['From'] = gmail.account
    return msg

def send_gmail(msg):
    server = smtplib.SMTP_SSL(
        'smtp.gmail.com', 465,
        context=ssl.create_default_context()
    )
    server.set_debuglevel(0)
    server.login(gmail.account, gmail.password)
    server.send_message(msg)
    
if __name__ == '__main__':
    body = """
    <h1>Gmailでメール送信する手順</h1>
    <ol>
        <li>Gmailのアプリパスワードの取得</li>
        <li>SMTPサーバの準備
            <ul>
                <li>ホスト名情報の入手</li>
                <li>ポート番号情報の入手</li>
            </ul>
        </li>
        <li>メール送信プログラムの作成</li>
        <li>メール送信</li>
    </ol>
    <address>教室のURL: <a href="https://haru-idea.jp/">haruプログラミング教室</a>
"""
    send_test_email(body)
    print('ok')
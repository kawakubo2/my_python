import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost'
}

try:
    dbconnector = mysql.connector.connect(**config)
except mysql.connector.Error as errmsg:
    print('MySQLサーバへの接続に失敗しました。')
    print('エラーメッセージ: ', errmsg)
else:
    print('MySQLサーバへの接続が成功しました。')
    dbconnector.close()

import mysql.connector

# MySQLのharulesson_yokochiに接続
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="harulesson_yokochi"
)
# カーソル
cursor = conn.cursor()

print("データベース接続が確立しました。")

cursor.close()
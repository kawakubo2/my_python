import pymysql


# Open local database connection
conn = pymysql.connect(host='localhost',
                     db='housekeeping',
                     user='root',
                     passwd='root',
                     port=3306,
                     charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql = "SELECT 日付, 費目, メモ, 入金額, 出金額 FROM 家計簿"
        cursor.execute(sql)
        for item in cursor.fetchall():
            print("{} {} {} {} {}".format(item[0], item[1], item[2], item[3], item[4]))
finally:
    conn.close()

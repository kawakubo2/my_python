from get_connect import get_connect

def create_table(create_sql, table_name):
    drop_sql = "DROP TABLE IF EXISTS {}".format(table_name)
    create_sql = create_sql.format(table_name)
    with get_connect() as connect:
        with connect.cursor() as cursor:
            cursor.execute(drop_sql)
            cursor.execute(create_sql)
        connect.commit()

if __name__ == "__main__":
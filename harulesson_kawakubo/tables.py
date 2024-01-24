from get_connect import get_connect

def drop_table(table_name):
    drop_sql = "DROP TABLE IF EXISTS {}".format(table_name)
    with get_connect() as connect:
        with connect.cursor() as cursor:
            cursor.execute(drop_sql)
        connect.commit()
    
def create_table(table_name, create_sql):
    drop_sql = "DROP TABLE IF EXISTS {}".format(table_name)
    create_sql = create_sql.format(table_name)
    with get_connect() as connect:
        with connect.cursor() as cursor:
            cursor.execute(drop_sql)
            cursor.execute(create_sql)
        connect.commit()

def delete_table(table_name):
    delete_sql = "DELETE FROM {}".format(table_name)
    with get_connect() as connect:
        with connect.cursor() as cursor:
            cursor.execute(delete_sql)
        connect.commit()

def insert_table(table_name, insert_sql, data):
    delete_sql = "DELETE FROM {}".format(table_name)
    insert_sql = insert_sql.format(table_name)
    with get_connect() as connect:
        with connect.cursor() as cursor:
            cursor.execute(delete_sql)
            cursor.executemany(insert_sql, data)
        connect.commit()


from get_connect import get_connect

def drop_table(connect, table_name):
    drop_sql = "DROP TABLE IF EXISTS {}".format(table_name)
    with connect.cursor() as cursor:
        cursor.execute(drop_sql)
    
def create_table(connect, table_name, create_sql):
    drop_sql = "DROP TABLE IF EXISTS {}".format(table_name)
    create_sql = create_sql.format(table_name)
    with connect.cursor() as cursor:
        cursor.execute(drop_sql)
        cursor.execute(create_sql)

def delete_table(connect, table_name):
    delete_sql = "DELETE FROM {}".format(table_name)
    with connect.cursor() as cursor:
        cursor.execute(delete_sql)

def insert_table(connect, table_name, insert_sql, data):
    insert_sql = insert_sql.format(table_name)
    with connect.cursor() as cursor:
        cursor.executemany(insert_sql, data)


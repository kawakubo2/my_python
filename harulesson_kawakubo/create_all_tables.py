from create_table import create_table

"""
依存性テーブルをスタックとして作成し、
依存しているデータとスキーマを再作成できるよう
create table と drop table
insert と delete
はそれぞれ分けて関数化したほうがいいかも
"""
def create_companies_table():
    create_sql = """CREATE TABLE {}(
            id INT NOT NULL AUTO_INCREMENT,
            会社名 VARCHAR(255) NOT NULL,
            住所 VARCHAR(255) NOT NULL,
            担当者名 VARCHAR(255) NOT NULL,
            担当者Eメール VARCHAR(255) NOT NULL,
            PRIMARY KEY(id)
        );
        """ 

create_companies_table(create_sql, "会社")

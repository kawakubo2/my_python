from tables import create_table, drop_table
from collections import deque

create_companies_sql = """CREATE TABLE {}(
        id INT NOT NULL AUTO_INCREMENT,
        会社名 VARCHAR(255) NOT NULL,
        住所 VARCHAR(255) NOT NULL,
        担当者名 VARCHAR(255) NOT NULL,
        担当者Eメール VARCHAR(255) NOT NULL,
        PRIMARY KEY(id)
    );
    """ 
create_students_sql = """CREATE TABLE {}(
        id INT NOT NULL AUTO_INCREMENT,
        名前 VARCHAR(255) NOT NULL,
        Eメール VARCHAR(255) NOT NULL,
        会社id INT,
        PRIMARY KEY(id),
        FOREIGN KEY(会社id) REFERENCES 会社(id)         
    );
    """
create_courses_sql = """CREATE TABLE {}(
        id INT NOT NULL AUTO_INCREMENT,
        名前 VARCHAR(255) NOT NULL,
        説明 VARCHAR(255),
        PRIMARY KEY(id)
    );
    """

operations = [
    {"name": "コース", "sql": create_courses_sql },
    {"name": "生徒", "sql": create_students_sql },
    {"name": "会社", "sql": create_companies_sql },
]

def create_all_tables():
    stack = deque()
    for operation in operations:
        stack.append(operation)
        drop_table(operation["name"])
    while stack:
        operation = stack.pop()
        create_table(operation["name"], operation["sql"])

if __name__ == "__main__":
    create_all_tables()
    print("テーブルの作成に成功しました。")


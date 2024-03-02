from tables import create_table, drop_table
from collections import deque
from get_connect import get_connect

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

create_unit_prices_sql = """CREATE TABLE {}(
        id INT NOT NULL AUTO_INCREMENT,
        生徒id INT NOT NULL,
        コースid INT NOT NULL,
        適用開始日 DATE NOT NULL,
        時間単価 INT NOT NULL,
        PRIMARY KEY(id),
        FOREIGN KEY(生徒id) REFERENCES 生徒(id),
        FOREIGN KEY(コースid) REFERENCES コース(id)
    );
    """

create_lesson_records_sql = """CREATE TABLE {}(
        id INT NOT NULL AUTO_INCREMENT,
        単価id INT NOT NULL,
        受講日 DATE NOT NULL,
        開始時刻 TIME NOT NULL,
        終了時刻 TIME NOT NULL,
        請求済みフラグ CHAR(1) DEFAULT '0' COMMENT '0: 未請求 1:請求済み',
        PRIMARY KEY(id),
        FOREIGN KEY(単価id) REFERENCES 単価(id)
    );
    """

operations = [
    {"name": "受講記録", "sql": create_lesson_records_sql },
    {"name": "単価", "sql": create_unit_prices_sql },
    {"name": "コース", "sql": create_courses_sql },
    {"name": "生徒", "sql": create_students_sql },
    {"name": "会社", "sql": create_companies_sql },
]

def create_all_tables():
    stack = deque()
    with get_connect() as connect:
        for operation in operations:
            stack.append(operation)
            drop_table(connect, operation["name"])
        while stack:
            operation = stack.pop()
            create_table(connect, operation["name"], operation["sql"])
        connect.commit()
        print("テーブルの作成に成功しました。")

if __name__ == "__main__":
    create_all_tables()


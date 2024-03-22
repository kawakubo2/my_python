from datetime import time
from collections import deque
from get_connect import get_connect
from tables import insert_table, delete_table
from create_dates import create_dates

companies = [
    (1, "福岡ソリューションズ", "福岡市中央区大中央1-2-3", "佐々木義男", "y-sasaki@fuk-sol.com"),
    (2, "博多システムテクノロジーズ", "福岡市博多区小博多4-5-6", "和田実", "m-wada@hakata-system.com"),
    (3, "ソフトウェア博多", "福岡市博多区中博多7-8-9", "内藤友美", "t-naito@software-hakata.com"),
]
insert_companies_sql = "INSERT INTO {} VALUES(%s, %s, %s, %s, %s);"

students = [
    (101, '山田太郎', 'taro@yamada.com', None),
    (102, '横山花子', 'hanako@yokoyama.com', None),
    (103, '田中一郎', 'ichiro@tanaka.com', None),
    (104, '猫山五郎', 'goro@nekoyama.com', None),
    (105, '後藤信', 'shin@goto.com', None),
    (106, '山本久美子', 'kumiko@yamamoto.com', 1),
    (107, '鈴木次郎', 'jiro@suzuki.com', 1),
    (108, '星山裕子', 'yuko@hoshiyama.com', 2),
    (109, '佐藤勝男', 'katsuo@sato.com', 2),    
    (110, '遠藤大翔', 'haruto@endo.com', 2),    
    (111, '山田太郎', 'taro2@yamada.com', None),    
    (112, '横山花子', 'hanako2@yokoyama.com', None),    
]
insert_students_sql = """
            INSERT INTO {}
            VALUES(%s, %s, %s, %s);
            """

courses = [
    (201, "Python初級", "制御構文、リスト、辞書、セット、内包表記、ファイル操作"),
    (202, "Python中級", "カプセル化、継承、ポリモーフィズム、データベース操作"),
    (203, "Python上級", "Webアプリ作成、生成AIを使用したアプリ、クローリングを使用したアプリ作成のいずれか"),
    (204, "SQL", "SELECT、INSERT、UPDATE、DELETE。グループ化、サブクエリ、テーブル結合"),
    (205, "Java初級", "制御構文と配列の操作、オブジェクト指向の概要"),
    (206, "Java中級", "カプセル化、継承、ポリモーフィズム、ファイル操作、ストリーム操作"),
    (207, "Java上級", "JSP/ServletまたはSpring Bootを使用したWebアプリ作成"),
    (208, "C#初級", "制御構文、リスト、辞書、セット、コレクションクラスの操作")
]
insert_courses_sql = """
            INSERT INTO {}
            VALUES(%s, %s, %s);
            """
from datetime import date
unit_prices = [
    (301, 103, 201, date(2024,4,1), time(12, 0), 2800),
    (302, 104, 204, date(2024,4,1), time(14, 0), 2800),
    (303, 101, 202, date(2024,4,1), time(18, 0), 3000),
    (304, 102, 207, date(2024,4,1), time(20, 0), 3300),
    (305, 105, 206, date(2024,5,1), time(12, 0), 3000),
    (306, 106, 205, date(2024,5,1), time(14, 0), 2500),
    (307, 107, 205, date(2024,5,1), time(14, 0), 2500),
    (308, 108, 201, date(2024,6,1), time(12, 0), 2200),
    (309, 109, 201, date(2024,6,1), time(12, 0), 2200),
    (310, 110, 201, date(2024,6,1), time(12, 0), 2200),
    (311, 110, 204, date(2024,6,2), time(12, 0), 2800),
    (312, 111, 204, date(2024,7,1), time(12, 0), 2800),
]
insert_unit_prices_sql = """
            INSERT INTO {}
            VALUES(%s, %s, %s, %s, %s, %s);
            """
"""
# 1 1人の生徒が1つのコースを4月1日から15回受ける
# 2, 3は同じ開始日だが、別の生徒が1回受ける
# 4 1人の生徒が1つのコースを4月1日から週2回、15回受ける
# 5 1人の生徒が1つのコースを5月1日から15回受ける
# 6, 7は2名同時受講 
# 8, 9, 10は3名同時受講
# 11は10と同じ生徒が別コースを同じ期間で受講する
# 12は1と同姓同名
"""
lesson_record_source_data = [
    { "unit_price_id": 301, "start_date": [ date(2024, 4, 1) ], "start_time": time(12, 0), "end_time": time(14, 0)}, #1
    { "unit_price_id": 302, "start_date": [ date(2024, 4, 1) ], "start_time": time(14, 0), "end_time": time(16, 0)}, #2
    { "unit_price_id": 303, "start_date": [ date(2024, 4, 1) ], "start_time": time(18, 0), "end_time": time(20, 0)}, #3
    { "unit_price_id": 304, "start_date": [ date(2024, 4, 1), date(2024, 4, 3) ], "start_time": time(20, 0), "end_time": time(22, 0)}, #4
    { "unit_price_id": 305, "start_date": [ date(2024, 5, 1) ], "start_time": time(12, 0), "end_time": time(14, 0)}, #5
    { "unit_price_id": 306, "start_date": [ date(2024, 5, 1) ], "start_time": time(14, 0), "end_time": time(16, 0)}, #6
    { "unit_price_id": 307, "start_date": [ date(2024, 5, 1) ], "start_time": time(14, 0), "end_time": time(16, 0)}, #7
    { "unit_price_id": 308, "start_date": [ date(2024, 6, 1) ], "start_time": time(12, 0), "end_time": time(14, 0)}, #8
    { "unit_price_id": 309, "start_date": [ date(2024, 6, 1) ], "start_time": time(12, 0), "end_time": time(14, 0)}, #9
    { "unit_price_id": 310, "start_date": [ date(2024, 6, 1) ], "start_time": time(12, 0), "end_time": time(14, 0)}, #10
    { "unit_price_id": 311, "start_date": [ date(2024, 6, 2) ], "start_time": time(12, 0), "end_time": time(14, 0)}, #11
    { "unit_price_id": 312, "start_date": [ date(2024, 7, 1) ], "start_time": time(12, 0), "end_time": time(14, 0)}, #12
]

def create_lesson_data(lesson_record_source_data):
    """コース1回分の日付のリストと、受講記録のもととなる辞書を使用して、受講記録は一括して登録する関数
    Parameters
    ----------
    lesson_record_source_data: list
            下記のキーを持つ辞書のリスト
            生徒id, コースid, 単価id, 受講を開始する曜日のリスト, 開始時刻, 終了時刻の辞書
            [補足]
            受講を開始する曜日のリストとは1週2回以上受講する場合、曜日ごとの初回日付のリストとなる。
            単一曜日の場合は要素が1個のリスト
    Returns
    -------
        list
            受講記録を登録するためのリスト
    """
    lesson_data = []
    lesson_record_id = 4001
    for data in lesson_record_source_data:
        dates = create_dates(data['start_date'])
        for date in dates:
            lesson_data.append((lesson_record_id, data["unit_price_id"], date, data['start_time'], data['end_time'], "0"))
            lesson_record_id += 1
    return lesson_data

insert_lesson_records_sql = """
            INSERT INTO {}
            VALUES (%s, %s, %s, %s, %s, %s);
            """

operations = deque([
    {"name": "受講記録", "sql": insert_lesson_records_sql, "data": create_lesson_data(lesson_record_source_data)},
    {"name": "単価", "sql": insert_unit_prices_sql, "data": unit_prices },
    {"name": "コース", "sql": insert_courses_sql, "data": courses },
    {"name": "生徒", "sql": insert_students_sql, "data": students},
    {"name": "会社", "sql": insert_companies_sql, "data": companies },
])

def insert_all_tables():
    with get_connect() as connect:
        for operation in operations:
            delete_table(connect, operation["name"])
        while operations:
            operation = operations.pop()
            insert_table(connect, operation["name"], operation["sql"], operation["data"])
        connect.commit()
        print("データの投入に成功しました。")

if __name__  == "__main__":
    insert_all_tables()
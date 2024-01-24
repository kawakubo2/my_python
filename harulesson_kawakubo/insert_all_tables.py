from get_connect import get_connect
from tables import insert_table, delete_table

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
    (207, "Java上級", "JSP/ServletまたはSpring Bootを使用したWebアプリ作成")
]
insert_courses_sql = """
            INSERT INTO {}
            VALUES(%s, %s, %s);
            """

def insert_all_tables():
    delete_table("コース")
    delete_table("生徒")
    delete_table("会社")
    insert_table("会社", insert_companies_sql , companies)
    insert_table("生徒",insert_students_sql,  students)
    insert_table("コース", insert_courses_sql, courses)

if __name__  == "__main__":
    insert_all_tables()
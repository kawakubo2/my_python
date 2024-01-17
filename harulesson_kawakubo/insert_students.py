from get_connect import get_connect

with get_connect() as connect:
    with connect.cursor() as cursor:
        companies = [
            (1, "福岡ソリューションズ", "福岡市中央区大博多1-2-3", "佐々木義男", "y-sasaki@fuk-sol.com"),
            (2, "博多システムテクノロジーズ", "福岡市博多区小博多4-5-6", "和田実", "m-wada@hakata-system.com"),
            (3, "ソフトウェア博多", "福岡市博多区中博多7-8-9", "内藤友美", "t-naito@softbankofhakata.com"),
        ]
        cursor.execute("DELETE FROM 会社;")
        cursor.executemany(
                """
                INSERT INTO 会社
                VALUES(%s, %s, %s, %s, %s)
                """, companies)
    connect.commit()
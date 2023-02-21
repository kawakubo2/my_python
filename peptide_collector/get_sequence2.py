import MySQLdb, os
"""
sequenceの末尾がKまたはRで終らないものの検索
"""
def main():
    get_sequences_without_k_or_r()

def get_sequences_without_k_or_r():
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='root',
        db = 'peptide_db'
    )
    cursor = connection.cursor()
    sql = """SELECT DISTINCT sequence
             FROM psms
             ORDER BY sequence"""
    cursor.execute(sql)

    for sequence, in cursor:
        if sequence[-1] not in ('K', 'R'):
            print(f"{sequence}")

    cursor.close()
    connection.close()

if __name__ == '__main__':
    main()
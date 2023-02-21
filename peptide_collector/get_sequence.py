import MySQLdb, os

def main():
    print("accessionに紐づくsequenceを検索します")
    accession = input("accessionを入力してください: ")
    get_sequences_by_accession(accession)

def get_sequences_by_accession(accession):
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='root',
        db = 'peptide_db'
    )
    cursor = connection.cursor()
    sql = """SELECT DISTINCT sequence
             FROM psms
             WHERE accession = '{}'
             ORDER BY sequence"""
    cursor.execute(sql.format(accession))

    for sequence, in cursor:
        print(f"{sequence}")

    cursor.close()
    connection.close()

if __name__ == '__main__':
    main()
import MySQLdb, os, glob

# load data命令用SQL文
sql_protein = """
LOAD DATA INFILE '{}' 
INTO TABLE proteins
CHARACTER SET utf8
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(protein_id, accession, symbol, name, protein_type, pep_count, psm_count, unique_pep_count)
"""

sql_psm = """
LOAD DATA INFILE '{}' 
INTO TABLE psms
CHARACTER SET utf8
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(psm_id, sequence, accession, exp_mz, calc_mz, charge, jpost_score)
"""

sql_psm_modification = """
LOAD DATA INFILE '{}' 
INTO TABLE psm_modifications
CHARACTER SET utf8
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(psm_id, modification, site, position)
"""

sql_delete_proteins = """
DELETE FROM proteins;
"""

sql_delete_psms = """
DELETE FROM psms;
"""
sql_delete_psm_modifications = """
DELETE FROM psm_modifications;
"""

input_path = '/temp/peptide/datasets'
filenames = {'protein.tsv': sql_protein, 'psm.tsv': sql_psm, 'psm_modification.tsv': sql_psm_modification}

def main():
    global sql_delete_proteins
    global sql_delete_psms
    global sql_delete_psm_modificatins
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='root',
        db = 'peptide_db'
    )
    cursor = connection.cursor()
    cursor.execute(sql_delete_proteins)
    connection.commit()
    cursor.execute(sql_delete_psms)
    connection.commit()
    cursor.execute(sql_delete_psm_modifications)
    connection.commit()
    for filename in filenames:
        insert_table_from_file(filename, cursor, connection)
    connection.close()

def insert_table_from_file(filename, cursor, connection):
    input_dir = '/temp/peptide/datasets'
    dirnames = glob.glob(input_dir + '/DS*')
    for dirname in dirnames:
        insert_data(os.path.join(dirname, filename), cursor, connection)
        # insert_data(dirname + '/' + filename, cursor, connection)

def insert_data(filename, cursor, connection):
    global filenames
    filename = filename.replace('\\', '/');
    basename = filename.split('/')[-1]
    sql = filenames[basename]
    print(f"filename={filename}")
    # print(f"basename={basename}")
    sql_temp = sql.format(filename)
    cursor.execute(sql_temp)
    connection.commit()

if __name__ == '__main__':
    main()
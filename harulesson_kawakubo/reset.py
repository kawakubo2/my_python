from create_all_tables import create_all_tables
from insert_all_tables import insert_all_tables

def reset():
    create_all_tables()
    insert_all_tables()

if __name__ == "__main__":
    try:
        reset()
    except Exception as e:
        print(e)
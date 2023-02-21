from product import Product
class FileProductProvider:
    def __init__(self):
        pass
    def create_products(self):
        product_dict = {}
        with open('products.txt', 'r', encoding='utf_8') as f:
            for line in f:
                ary = line.rstrip('\n').split('\t')
                code = ary[0]
                p = Product(ary[0], ary[1], ary[2], float(ary[3]))
                product_dict[code] = p
        return product_dict

import mysql.connector
class DBProductProvider:
    def __init__(self):
        pass
    def create_products(self):
        product_dict = {}

        config = {
            'host': 'localhost',
            'port': '3306',
            'user': 'root',
            'password': 'root',
            'database': 'kiso_python_netshop_imai'
        }
        conn = mysql.connector.connect(**config)

        if not conn.is_connected():
            print('データベースへの接続に失敗しました。')
            exit(1)

        cursor = conn.cursor(buffered=True)

        cursor.execute("SELECT code, name, info, unit_price FROM products")
        results = cursor.fetchall()
        for result in results:
            code = result[0]
            product = Product(result[0], result[1], result[2], float(result[3]))
            product_dict[code] = product

        conn.close()

        return product_dict

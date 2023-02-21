from product import Product

class ProductProvider:
    def __init__(self):
        pass

    def get_products(self):
        pass

class HardcodeProductProvider(ProductProvider):
    def __init__(self):
        pass

    def get_products(self):
        products = {
            'K16':Product("K16", "Wood screws", "brass 20mm pack of 50", 7.75),
            'D24':Product("D24", "Wood glue", "clear 1 letter", 5.50),
            'M93':Product("M93", "Sand paper(M)", "medium grade 100 sheets", 10.25),
            'M94':Product("M94", "Sand paper(F)", "fine grade 100 sheet", 14.75),
        }
        return products

class FileProductProvider(ProductProvider):
    def __init__(self):
        pass

    def get_products(self):
        products = []
        with open('products.txt', 'r', encoding='utf_8') as f:
            for line in f:
                ary = line.rstrip('\n').split(',')
                products.append(Product(ary[0], ary[1], ary[2], float(ary[3])))
        return products

class ProductViewer:
    def disp_poducts(self, products):
        print('--------------< 製品リスト >--------------------')
        print('コード\t製品名\t\t製品情報\t\t\t\t単価')
        for code, product in products.items():
            print('{:3}   {:20}  {:40} {:.2f}'.format(code, product.name, product.desc, product.unit_price))

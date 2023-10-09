import os
import sys
from abc import abstractmethod, ABC

class Product():
    def __init__(self, code, name, desc, unit_price):
        self.__code = code
        self.__name = name
        self.__desc = desc
        self.__unit_price = unit_price

    def get_code(self):
        return self.__code
    def get_name(self):
        return self.__name
    def get_desc(self):
        return self.__desc
    def get_unit_price(self):
        return self.__unit_price

    code = property(get_code)
    name = property(get_name)
    desc = property(get_desc)
    unit_price = property(get_unit_price)
    
    
    def __str__(self):
        return f"code={self.code}, name={self.name}, desc={self.desc}, unit_price={self.unit_price}"

class AbstractProductsProducer(ABC):
    @abstractmethod
    def get_products(products):
        pass

class ProductsProducerFromHardcode(AbstractProductsProducer):
    def get_products(self):
        products = {}
        products["K16"] = Product("K16", "Wood Screw", "aaa", 7.50)
        products["D24"] = Product("K24", "Wood Glue", "bbb", 11.00)
        return products

class ProductsProducerFromFile(AbstractProductsProducer):
    def get_products(self):
        products = {}
        with open(os.path.join(os.path.dirname(__file__), "products.txt"), "r") as f:
            for line in f:
                cols = line.split(",")
                products[cols[0]] = Product(cols[0], cols[1], cols[2], float(cols[3]))
        return products

class ProductsViewer():
    def view(__self, products):
        """
        製品情報を一覧として表示
        Parameters
        ----------
        products: dict<str, Product>
            キーが製品コード、値が製品インスタンスである辞書
            
        Returns
        -------
            なし
        """
        print("code    name                description           unit price")
        for code, product in products.items():
            print(f"{code:<8}{product.name:<20}{product.desc:<24}{product.unit_price:>8.2f}")

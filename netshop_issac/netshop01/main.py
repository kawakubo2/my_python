import os
from product import Product, \
    ProductsProducerFromFile, \
    ProductsViewer
from customer import ConsoleCustomerInputHelper
from order import ConsoleOrderInputHelper

if __name__ == "__main__":
    product_dict = ProductsProducerFromFile().get_products()
    ProductsViewer().view(product_dict)
    customer = ConsoleCustomerInputHelper().create()
    print("---注文(入力)開始---")
    order = ConsoleOrderInputHelper().create(customer)
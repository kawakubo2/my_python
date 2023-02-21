from product import Product
from product_provider import DBProductProvider
from product_viewer import ProductViewer 

product_dict = DBProductProvider().create_products()
ProductViewer(product_dict).view()
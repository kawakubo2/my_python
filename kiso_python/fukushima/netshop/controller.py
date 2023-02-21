from product import Product
from product_provider import HardcodeProductProvider, ProductViewer
from customer import CustomerCreator
from order import Order, OrderPrompt
from bill import Bill, ConsoleBillViewer


if __name__ == '__main__':
    product_pv = HardcodeProductProvider()
    products = product_pv.get_products()
    ProductViewer().disp_poducts(products)    
    customer = CustomerCreator().get_customer()
    order = Order(customer)
    OrderPrompt(order, products).input_item()
    bill = Bill(order, products)
    ConsoleBillViewer(bill, products).view()
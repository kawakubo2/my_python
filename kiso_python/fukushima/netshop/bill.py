class Bill:
    def __init__(self, order, product_dic):
        self.__order = order
        self.__product_dic = product_dic

    def get_order(self):
        return self.__order

    order = property(get_order)

class BillViewewr:
    def __init__(self, bill, product_dic):
        self.bill = bill
        self.product_dic = property

    def view(self):
        self.header()
        self.detail()
        self.footer()

    def header(self):
        pass
    def detail(self):
        pass
    def footer(self):
        pass

class ConsoleBillViewer(BillViewewr):
    def header(self):
        customer = self.bill.order.customer
        print(customer.name)
        print(customer.address1)
        print(customer.address2)
        print(customer.zipcode)
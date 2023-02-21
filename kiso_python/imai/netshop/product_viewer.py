class ProductViewer:
    def __init__(self, product_dict):
        self.product_dict = product_dict

    def view(self):
        print('code name               desc                           unit price')
        print('-----------------------------------------------------------------')
        for _, p in self.product_dict.items():
            print('{:4} {:18} {:30} {:.2f}'.format(p.code, p.name, p.desc, p.unit_price))
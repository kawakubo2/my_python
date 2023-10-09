class Invoice():
    def __init__(self, customer, product_dict):
        self.customer = customer
        self.product_dict = product_dict
        
    def get_customer(self):
        return self.customer
    
    def get_product_dict(self):
        return self.product_dict
    
    customer = property(get_customer)
    product_dict = property(get_product_dict)


        
    
class Order:
    def __init__(self, customer):
        self.__customer = customer
        self.__cart = dict()

    def add_product(self, code, amount):
        self.__cart[code] = amount

    def get_cart(self):
        return self.__cart

    def get_customer(self):
        return self.__customer
        
    customer = property(get_customer)

class OrderPrompt:
    def __init__(self, order, product_dic):
        self.__order = order
        self.__product_dic = product_dic
    

    def input_item(self):
        while True:
            while True:
                code = input('コード: ')
                if code == 'XX':
                    return
                if code in self.__product_dic:
                    break
            while True:
                amount = input('数量: ')
                try:
                    amount = int(amount)
                    if 1 <= amount <= 99:
                        break
                except:
                    print('正の整数を入力してください')
            
            self.__order.add_product(code, amount)
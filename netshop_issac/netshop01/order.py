from abc import abstractmethod, ABC

class Order():
    def __init__(self, customer):
        self.__customer = customer
        self.__order_detail = {}
        
    def get_customer(self):
        return self.__customer

    customer = property(get_customer)
    
    def add_item(self, product_code, quantity):
        if product_code in self.__order_detail:
            print("カートには同じ商品があります")
            if input("数量を置き換える場合はY、キャンセルするばあいはN: ") in ("Y", "y"):
                self.__order_detail[product_code] = quantity
        else:
            self.__order_detail[product_code] = quantity

class OrderInputHelper(ABC):
    @abstractmethod
    def create(self, customer):
        pass
    
class ConsoleOrderInputHelper(OrderInputHelper):
    def create(self, customer):
        order = Order(customer)
        while True:
            product_code = input("製品コード: ")
            if product_code in ("XX", "xx"):
                break
            quantity = int(input("個数: "))
            order.add_item(product_code, quantity)
        return order
from abc import abstractmethod, ABC

__all__ = [
    "Customer",
    "AbstracCustomerInputHelper",
    "ConsoleCustomerInputHelper"
]
class Customer():
    def __init__(self, name, address1, address2, zipcode):
        self.__name = name
        self.__address1 = address1
        self.__address2 = address2
        self.__zipcode = zipcode
        
    def get_name(self):
        return self.__name
    def get_address1(self):
        return self.__address1
    def get_address2(self):
        return self.__address2
    def get_zipcode(self):
        return self.__zipcode

    def __str__(self):
        return f"name={self.name}, address1={self.address1}, address2={self.address2}, zipcode={self.zipcode}"
    
    name = property(get_name) 
    address1 = property(get_address1)
    address2 = property(get_address2)
    zipcode = property(get_zipcode)


class AbstracCustomerInputHelper(ABC):
    @abstractmethod
    def create(self):
        pass

class ConsoleCustomerInputHelper(AbstracCustomerInputHelper):
    def create(self):
        name = input("名前: ")
        address1 = input("住所1: ")
        address2 = input("住所2: ")
        zipcode = input("郵便番号: ")
        return Customer(name, address1, address2, zipcode)

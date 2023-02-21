class Customer:
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

    name = property(get_name)
    address1 = property(get_address1)
    address2 = property(get_address2)
    zipcode = property(get_zipcode)

class CustomerCreator:
    def __init__(self):
        pass

    def get_customer(self):
        return Customer(input('名前:'), input('住所1'), input('住所2'), input('郵便番号'))

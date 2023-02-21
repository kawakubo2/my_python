class Product:
    def __init__(self, code, name, desc, unit_price):
        self.__code = code
        self.__name = name
        self.__desc = desc
        self.__unit_price = unit_price

    def get_code(self):
        return self.__code
    def get_name(self):
        return self.__name
    def get_desc(self):
        return self.__desc
    def get_unit_price(self):
        return self.__unit_price

    code = property(get_code)
    name = property(get_name)
    desc = property(get_desc)
    unit_price = property(get_unit_price)


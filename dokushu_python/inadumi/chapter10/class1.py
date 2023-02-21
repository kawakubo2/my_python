class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def show(self):
        print(f"私の名前は{self.lastname}{self.firstname}です！")

if __name__ == '__main__':
    p = Person('太郎', '山田')
    p.show()

    def abc(self):
        print(f'名前は{self.firstname}です!')

    Person.show_first = abc
    p.show_first()

    Person.show_last = lambda self: print(f'苗字は{self.lastname}です！')
    p.show_last()
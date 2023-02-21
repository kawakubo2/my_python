class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def get_firstname(self):
        return self.__firstname
    def set_firstname(self, firstname):
        self.__firstname = firstname
    def get_lastname(self):
        return self.__lastname
    def set_lastname(self, lastname):
        self.__lastname = lastname
    
    def show(self):
        print(f"私の名前は{self.lastname}{self.firstname}です！")

    firstname = property(get_firstname, set_firstname)
    lastname = property(get_lastname, set_lastname)
    
class PersonList:
    def __init__(self):
        self.data = []
    def add(self, person):
        self.data.append(person)
    def __iter__(self):
        return iter(self.data)
    
if __name__ == '__main__':
    pl = PersonList()
    pl.add(Person('太郎', '山田'))
    pl.add(Person('奈美', '掛谷'))
    pl.add(Person('悟助', '田中'))
    
    for p in pl:
        p.show() 
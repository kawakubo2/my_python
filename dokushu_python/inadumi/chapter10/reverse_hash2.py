class Person:
    __slots__ = ['__firstname', '__lastname']
    def __init__(self, firstname, lastname):
        self.__firstname = firstname
        self.__lastname = lastname

    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname

    """
    @firstname.setter
    def firstname(self, firstname):
        self.__firstname = firstname

    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname
    """

    def __delattr__(self, name):
        raise RuntimeError

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.firstname == other.firstname \
               and self.lastname == other.lastname
        return False

    def __hash__(self):
        return hash((self.firstname, self.lastname))

if __name__ == '__main__':
    p1 = Person('太郎', '山田')
    p2 = Person('花子', '横山')

    print(hash(('太郎', '山田')))
    print(hash(('太郎', '山田')))

    people = {}
    people[p1] = 32
    people[p2] = 40

    # p1.lastname = '田中'
    print(people.get(p1))
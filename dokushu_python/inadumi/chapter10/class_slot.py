class Person:
    __slots__ = ['firstname', 'lastname', 'age']
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def __str__(self):
        return f"firstname = {self.firstname}, age = {self.age}"
if __name__ == '__main__':
    p = Person('太郎', '山田')
    p.age = 18
    # p.height = 178
    del p.lastname
    print(p)

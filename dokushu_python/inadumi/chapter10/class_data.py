import dataclasses

@dataclasses.dataclass(frozen=True)
class Person:
    firstname: str
    lastname: str
    age: int = 0
    
    def show(self):
        print(f'私の名前は{self.lastname}{self.firstname}です。')
        
if __name__ == '__main__':
    p1 = Person('太郎', '山田', 58) # __init__
    p2 = Person('太郎', '山田', 58) # __init__
    print(p1) # __repr__
    print(p1 == p2) # __eq__
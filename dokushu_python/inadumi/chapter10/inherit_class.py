class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def show(self):
        print(f'私の名前は{self.lastname}{self.firstname}です。')

class BusinessPerson(Person):
    def work(self):
        print(f'{self.lastname}{self.firstname}は働いています。')

class EliteBusinessPerson(BusinessPerson):
    def work(self):
        print(f'{self.lastname}{self.firstname}はバリバリ働いています。')

class HetareBusinessPerson(BusinessPerson):
    def work(self):
        super().work()
        print('ただし、ボチボチと・・・')

class Foreigner(Person):
    def __init__(self, firstname, middlename, lastname):
        super().__init__(firstname, lastname)
        self.middlename = middlename

    def show(self):
        print(f"私の名前は{self.lastname}・{self.middlename}・{self.firstname}です！")

if __name__ == '__main__':
    bp = BusinessPerson('太郎', '山田')
    bp.work()
    bp.show()
    
    ebp = EliteBusinessPerson('太郎', '山田')
    ebp.work()
    ebp.show()

    hbp = HetareBusinessPerson('太郎', '山田')
    hbp.work()
    hbp.show()

    fr =  Foreigner('太郎', 'ヨーダ', '山田')
    fr.show()
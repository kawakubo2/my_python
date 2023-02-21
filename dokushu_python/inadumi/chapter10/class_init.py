import types
# 動的に追加するメソッドを準備
def show_first(self):
    print(f"名前は{self.firstname}です。")

def show_last(self):
    print(f"苗字は{self.lastname}です。")


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

if __name__ == '__main__':
    p1 = Person('太郎', '山田')
    p2 = Person('次郎', '鈴木')
    # メソッドを動的に追加
    Person.show_first = show_first
    p1.show_last = types.MethodType(show_last, p1)
    p1.show_first()
    p1.show_last()
    p2.show_first()
    # p2.show_last()
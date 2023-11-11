"""
クラスは設計図
"""
class Person():
    """
    __init__メソッドを特殊メソッドと呼ぶ
    特殊メソッドは自分で呼び出すものではなく、あるタイミングで呼び出される
    メソッドのことを指す
    特に__init__メソッドをコンストラクタと言う。
    """
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    # 引数にselfを取るメソッドをインスタンスメソッドと呼ぶ
    def get_name(self):
        return self.lastname + self.firstname

# クラスからインスタンスを生成することをインスタンス化と呼ぶ
# Person(...)を呼び出すとPersonクラスの__init__メソッドが呼び
# 出される。下の例ではp1やp2がインスタンス。
p1 = Person("一郎", "田中")
p2 = Person("花子", "横山")

print(p1.get_name())
print(p2.get_name())
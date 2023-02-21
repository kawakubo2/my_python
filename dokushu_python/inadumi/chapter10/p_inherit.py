class MyClass:
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name
    def show(self):
        return f"ペットの{self.kind}の名前は、{self.name}です。"

class MySubClass(MyClass):
    def show(self):
        return f"<h1>{super().show()}</h1>";


if __name__ == '__main__':
    msc = MySubClass("犬", "ポチ")
    print(msc.show())
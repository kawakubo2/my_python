class Hamster:
    """
    nameを持ったハムスターを表すクラス
    """
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def show(self, fmt):
        """
        引数で受け取った書式文字列にnameを埋め込み、コンソールに表示する
        """
        print(fmt.format(self.name))

if __name__ == '__main__':
    ham = Hamster('太郎')
    print(ham.__doc__)
    print(Hamster.__name__)
    ham.show('私が飼っているハムスターの名前は{}です。')
    print(ham.show.__doc__)
    
    x = Hamster
    print(type(x.__name__))
    ham2 = x('花子')
    ham2.show('私の名前は{}です。')
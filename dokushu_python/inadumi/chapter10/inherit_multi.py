class TopA:
    def hoge(self):
        print('TopA')

class TopB:
    def hoge(self):
        print('TopB')

class MiddleA(TopA, TopB):
    def hoge(self):
        print('MiddleA')

class MiddleB(TopA, TopB):
    def hoge(self):
        print('MiddleB')

class Low(MiddleA, MiddleB):
    pass

l = Low()
l.hoge()

print(Low.mro())
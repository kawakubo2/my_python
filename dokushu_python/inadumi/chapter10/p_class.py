class Pet:
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name
    def show(self):
        print(f'私のペットは{self.kind}の{self.name}ちゃんです！')

if __name__ == '__main__':
    p = Pet('ハムスター', 'ハム太郎')
    p.show()
class my_class:
    def hello(self):
        print('Hello ', end="")

class my_class2(my_class):
    def hello(self, name = "World"):
        super().hello()
        print(name, end="")

if __name__ == '__main__':
    my = my_class2()
    my.hello()
    print('')
    my.hello("Python")
    print('')

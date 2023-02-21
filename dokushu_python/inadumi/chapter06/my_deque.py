class MyDequeue:
    NUM = 5
    def __init__(self):
        self.head = self.tail = 0
        self.size = 0
        self.array = [''] * MyDequeue.NUM

    def add_last(self, n):
        if self.size >= MyDequeue.NUM:
            print('キューは満杯です')
            return
        self.array[self.tail] = n
        self.tail = (self.tail + 1 % MyDequeue.NUM)
        self.size += 1

    def remove_first(self):
        if self.size == 0:
            print('キューは空です')
            return
        self.head = (self.head + 1 % MyDequeue.NUM)
        self.size -= 1

    def print_array(self):
        if self.head < self.tail:
            for i in range(MyDequeue.NUM):
                if (i >= self.head and i <= self.tail): print('{} '.format(self.array[i]), end='')
                else: print('- ', end='')
        elif self.head >= self.tail:
            for i in range(MyDequeue.NUM):
                if (i <= self.tail or i > self.head):
                    print('- ', end='')
                else:
                    print('{} '.format(self.array[i]), end='')
        print()

if __name__ == '__main__':
    mydequeue = MyDequeue()
    while True:
        sw = int(input("1.末尾に追加 2.先頭から削除 3.全体を表示 9.終了: "))
        if sw == 1:
            num = int(input('整数値: '))
            mydequeue.add_last(num)
            mydequeue.print_array()
        elif sw == 2:
            mydequeue.remove_first()
            mydequeue.print_array()
        elif sw == 3:
            mydequeue.print_array()
        elif sw == 9:
            break
        else:
            print("1,2,3,9の中から選択してください。")

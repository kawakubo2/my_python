class Stack(list):

    def push(self, elem):
        self.append(elem)

    def insert(self, elam):
        raise RuntimeError()

stack = Stack()
stack.push('A')
print(stack)
stack.push('B')
print(stack)
stack.push('C')
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.push('D')

pos = stack.insert('E')
print(pos)
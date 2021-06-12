class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    def peek(self):
        return self.stack[-1]

obj = Stack()

obj.add('Mon')
obj.add('Tue')
obj.add('Wed')

print(obj.peek())

obj.add('Thu')
obj.add('Fri')

print(obj.peek())
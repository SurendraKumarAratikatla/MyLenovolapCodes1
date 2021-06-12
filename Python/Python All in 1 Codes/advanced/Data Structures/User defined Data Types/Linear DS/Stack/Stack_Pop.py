class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    def remove(self):
        if len(self.stack) < 0:
            return f"no elements in Stack"
        else:
            return self.stack.pop()

obj = Stack()

obj.add('SAT')
obj.add('SUN')
obj.add('MON')

print(obj.stack)

print(obj.remove())

print(obj.stack)


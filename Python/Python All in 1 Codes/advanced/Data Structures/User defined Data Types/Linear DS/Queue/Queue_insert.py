class Queue:
    def __init__(self):
        self.queue = []

    def addtoq(self,dataval):
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        else:
            return False

    def size(self):
        return len(self.queue)

obj = Queue()

obj.addtoq('jan')
obj.addtoq('feb')
obj.addtoq('march')

print(obj.queue)

print(obj.size())




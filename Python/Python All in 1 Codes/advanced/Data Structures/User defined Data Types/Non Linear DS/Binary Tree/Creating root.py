class Node:
    def __init__(self, data):
        self.leftnode = None
        self.righnode = None
        self.data = data

    def PrintTree(self):
        return self.data


obj = Node(10)
print(obj.PrintTree())



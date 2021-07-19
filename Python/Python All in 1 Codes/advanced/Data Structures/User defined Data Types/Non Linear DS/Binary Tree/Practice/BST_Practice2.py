class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if self.data == data:
            return
        elif self.data > data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def search(self,val):
        if self.data == val:
            return True
        elif self.data > val:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False


def built_tree(numbers):
    root = BinarySearchTree(numbers[0])
    for value in range(1, len(numbers)):
        root.add_child(numbers[value])
    return root

if __name__ == '__main__':
    numbers = [4,1,20,9,23,18,34]
    bst_numbers = built_tree(numbers)
    print(bst_numbers.in_order_traversal())
    print(bst_numbers.search(232))

class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return
        elif data < self.data:
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


    # def search(self,val):
    #     left_index = 0
    #     right_index = len(sort_elements) - 1
    #     while left_index <= right_index:
    #         mid_index = (left_index + right_index) // 2
    #         mid_val = sort_elements[mid_index]
    #         if mid_val == val:
    #             return mid_index
    #         elif mid_val > val:
    #             right_index = mid_index - 1
    #         else:
    #             left_index = mid_index + 1
    #     return -1

    # or

    def search(self, val):
        if self.data == val:
            return True

        elif val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self







def built_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34]
    numbers_tree = built_tree(numbers)
    print(numbers_tree.in_order_traversal())
    # print(numbers_tree.search(23))
    # print(numbers_tree.find_max())
    # print(numbers_tree.find_min())
    numbers_tree.delete(18)
    print(numbers_tree.in_order_traversal())









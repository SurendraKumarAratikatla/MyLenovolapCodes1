class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            return f"linkedlist is empty"

        else:
            itr = self.head
            llstr = ''
            while itr:
                llstr += str(itr.data) + '------>'
                itr = itr.next
            print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)

    def lllength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count


    def remove_at(self,index):
        if index < 0 or index > self.lllength():
            raise Exception("Invalid Index passed")
        elif index == 0:
            self.head = self.head.next

        else:
            count = 0
            itr = self.head
            while itr:
                if count == index-1:
                    itr.next = itr.next.next
                    break
                count += 1

    def insert_at(self,index, data):
        if index < 0 or index > self.lllength():
            raise Exception("Invalid Index passed")

        elif index == 0:
            node = Node(data, self.head)
            self.head = node

        else:
            count = 0
            itr = self.head
            while itr:
                if count == index -1:
                    node = Node(data, itr.next)
                    itr.next = node
                    break
                count += 1



ll = LinkedList()
ll.insert_at_begining("23")
ll.insert_at_begining("12")
ll.insert_at_begining("34")
ll.insert_at_end("99")
ll.insert_at_end("55")
ll.insert_at_end("100")
ll.print()
ll.insert_at(1,88)
#print(ll.lllength())
ll.print()
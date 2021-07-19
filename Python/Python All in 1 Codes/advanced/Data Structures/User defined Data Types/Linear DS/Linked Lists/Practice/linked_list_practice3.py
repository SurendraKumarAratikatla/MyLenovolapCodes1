class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # insertion
    def insert_at_begining(self,data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_ending(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def length_all(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_middle(self,index, data):
        if index < 0 or index > self.length_all():
            raise Exception("Invalid index")
        elif index == 0:
            self.insert_at_begining(data)
        count = 0
        itr = self.head
        while itr:
            if index - 1 == count:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    # deletion
    def delete_at_begining(self):
        self.head = self.head.next

    def delete_at_ending(self):
        count = 0
        itr = self.head
        #while itr:
        # or
        while itr.next:
            if count == self.length_all() - 2:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def delete_at_middle(self, index):
        if index < 0 or index > self.length_all():
            raise Exception("Invalid index")
        elif index == 0:
            self.delete_at_begining()
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index-1:
                    itr.next = itr.next.next
                itr = itr.next
                count += 1

    def printll(self):
        count = 0
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + str("----->")
            itr = itr.next
        print(llstr)

ll = LinkedList()
ll.insert_at_begining(20)
ll.insert_at_begining(11)
ll.insert_at_ending(33)
ll.insert_at_ending(102)
ll.insert_at_ending(202)
ll.insert_at_ending(55)
# ll.insert_at_middle(3, 101)
# ll.delete_at_begining()
# ll.delete_at_ending()
# ll.delete_at_middle(2)
ll.printll()

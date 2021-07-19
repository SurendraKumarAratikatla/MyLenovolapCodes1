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

    def insert_at_ending(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_list_values(self,values):
        for value in values:
            ll.insert_at_ending(value)

    def length_all(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self,index):
        if index < 0 or index > self.length_all():
            raise Exception("Invalid Index")
        elif index == 0:
            self.head = self.head.next
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count += 1

    def insert_at(self,index,data):
        if index < 0 or index > self.length_all():
            raise Exception("Invalid index")
        elif index == 0:
            self.insert_at_begining()
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    node = Node(data, itr.next)
                    itr.next = node
                itr = itr.next
                count += 1


    def print(self):
        count = 0
        llstr = ''
        itr = self.head
        while itr:
            llstr += str(itr.data) + "---->"
            itr = itr.next
        print(llstr)

ll = LinkedList()
ll.insert_at_begining(23)
ll.insert_at_begining(45)
ll.insert_at_begining(11)
# ll.insert_at_ending(23)
# ll.insert_at_ending(45)
# ll.insert_at_ending(11)

# ll.insert_list_values([1,2,3,4,5,6,7,8,9])

ll.print()
ll.insert_at(2,100)
ll.print()
print(ll.length_all())



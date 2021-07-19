class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    # def head1(self):
    #     itr = self.head
    #     while itr:
    #         print(itr.data)
    #         itr = itr.next

    def print(self):
        if self.head is None:
            return f'my likedlist is empty'
        else:
            itr = self.head
            liklist_str = ''
            while itr:
                liklist_str += str(itr.data) +"------->"
                itr = itr.next

        print(liklist_str)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)

    def insert_values(self,data_list):
        for value in data_list:
            ll.insert_at_end(value)

    def lenght_ll(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        #print(count)
        return count

    def remove_at(self,index):
        if index < 0 or index > self.lenght_ll():
            raise Exception("Invalid index")

        elif index == 0:
            self.head = self.head.next

        else:
            count = 0
            itr = self.head
            while itr:
                if count == index-1:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count += 1


    def insert_at(self,index, data):
        if index < 0 or index > self.lenght_ll():
            raise Exception("Invalid index")

        elif index == 0:
            self.insert_begining(data)

        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    node = Node(data, itr.next)
                    itr.next = node
                itr = itr.next
                count +=1

ll = LinkedList()
ll.insert_values(["a","b","c","d"])
print(ll.lenght_ll())
#ll.head1()
ll.print()
ll.insert_at(3, "e")
ll.print()


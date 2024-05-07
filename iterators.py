#  Python program to implement Singly Linked List with iterators


class Node:
    def __init__ (self,data=None):
        self.data=data
        self.next=None

class Singlylinkedlist:
    def __init__(self):
        self.head=None

    def prepend(self,data):
        new_node = Node(data)
        new_node.next=self.head
        self.head=new_node

    def __iter__(self):
        self.current=self.head
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        data=self.current.data
        self.current=self.current.next
        return data
    

# diver Code 
    

mylist=Singlylinkedlist()
mylist.prepend(99)
mylist.prepend(83)
mylist.prepend(43)
mylist.prepend(92)
mylist.prepend(2)
mylist.prepend(14)
mylist.prepend(21)

for x in mylist:
    print(x)
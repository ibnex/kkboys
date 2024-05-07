# Python program to implement Doubly Linked List with operations for prepending nodes, appending 
# nodes, traversing


class Node:
    def __init__ (self,data=None):
        self.data=data
        self.next=None
        self.prev=None

class Doublylinkedlist:
    def __init__(self):
        self.head=None


    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
            new_node.prev=current

    
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        if self.head:
            self.head.prev=new_node
        self.head=new_node


    def traverse_forward(self):
        current=self.head
        while current:
            print(current.data, end="->")
            current=current.next
        print("None")

    def traverse_backward(self):
        current=self.head
        while current and current.next:
            current=current.next

        while current:
            print(current.data, end=" ->")
            current=current.prev
        print("None")




# driver Code 


mylist=Doublylinkedlist()

mylist.append(1)
mylist.append(2)
mylist.append(3)


mylist.prepend(0)

print("traversing forward:")
mylist.traverse_forward()

print("traversing backward:")
mylist.traverse_backward()

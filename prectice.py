class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class iterator:
    def __init__(self):
        self.head=None

    def prepend(self):
        new_node=Node(data)
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
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1
    
    def print_queue(self):
        temp=self.first
        while temp:
            print(temp.value)
            temp=temp.next

    def enqueue(self,value):
        new_node=Node(value)
        if self.length==0:
            self.first=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
        self.length+=1

    def dequeue(self):
        if self.length==0:
            return None
        elif self.length==1:
            self.first=None
            self.last=None
        else:
            temp=self.first
            self.first=self.first.next
            temp.next=None
        self.length-=1
        return temp.value

queue1 =Queue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(4)
queue1.print_queue()
print('\n')

print(queue1.dequeue())
print('\n')
queue1.print_queue()
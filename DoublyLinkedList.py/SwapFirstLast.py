#DLL: Swap First and Last ( ** Interview Question)
#Swap the values of the first and last node

# Method name:
# swap_first_last

# Note that the pointers to the nodes themselves are not swapped - only their values are exchanged.

class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        return True
    
    def swap_first_last(self):
        # 1. Check if the doubly linked list is empty or has only one node.
        # If so,there's nothing to swap,hence exit the function.
        if self.head is None or self.head==self.tail:
            return
        
        # 2. If the list has more than one node,swap the values of the head(first node)
        # and tail(last node). 
        # Note: We're only exchanging the data stored in the nodes,rather than alerting the structure of the linked list itself.
        self.head.value,self.tail.value=self.tail.value,self.head.value

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)


print('DLL before swap_first_last():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.swap_first_last()


print('\nDLL after swap_first_last():')
my_doubly_linked_list.print_list()

   
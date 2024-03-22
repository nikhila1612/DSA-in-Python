class Node:
    def __init__(self,value):
        # Store node value
        self.value=value
        # Reference to next node
        self.next=None
        #Reference to previous node
        self.prev=None

class DoublyLinkedList:
    def __init__(self,value):
        # Create new node with value
        new_node=Node(value)
        # Set head to new node
        self.head=new_node
        # Set tail to new node
        self.tail=new_node
        # Set initial length to 1
        self.length=1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self,value):
        # Create a new node with the given value
        new_node=Node(value)
        # Check if the list is empty(head is None)
        if self.head is None:
            # Set head and tail to the new node
            self.head=new_node
            self.tail=new_node
        else:
            # Connect the new node to the end of the list
            self.tail.next=new_node
            # Connect the new node to the previous node
            new_node.prev=self.tail
            # Update the tail to point to the new node
            self.tail=new_node
        # Increment the length of the list
        self.length+=1
        # Return True to indicate success
        return True
    
    def pop(self):
        # Check if the list has no nodes
        if self.length==0:
            # Return None to indicate an empty list
            return None
        # Store the tail node in 'temp' variable
        temp = self.tail
        # If list has just one node
        if self.length==1:
            # Set head and tail to None, making list empty
            self.head=None
            self.tail=None
        else:
            # Set the tail to the node before the current tail
            self.tail =self.tail.prev
            # Remove link to last node by setting next to None
            self.tail.next=None
            # Detach the popped node from the list
            temp.prev=None
            # Decrement list length by 1 to reflect removal
        self.length-=1
        # Return the removed node
        return temp
    
    def prepend(self,value):
        new_node=Node(value)
        if self.length ==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length +=1
        return True
    
    def pop_first(self):
        if self.length ==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head =self.head.next
            self.head.prev=None
            temp.next=None
        self.length-=1
        return temp
    
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        if index < self.length/2:
            temp=self.head
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        return temp
    
    def set_value(self,index,value):
        temp=self.get(index)
        if temp is not None:
            temp.value=value
            return True
        return False
    
    def insert(self,index,value):
        new_node=Node(value)
        if index < 0 or index >self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        before=self.get(index-1)
        after=before.next
        new_node.next=after
        new_node.prev=before
        after.prev=new_node
        before.next=new_node
        self.length+=1
        return True
    
    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        
        temp=self.get(index)

        temp.next.prev=temp.prev
        temp.prev.next=temp.next
        temp.next=None
        temp.prev=None

        self.length-=1
        return temp



    
    
my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(21)
my_doubly_linked_list.prepend(10)
my_doubly_linked_list.remove(1)
my_doubly_linked_list.print_list()

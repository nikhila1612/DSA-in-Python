#LL: Has Loop ( ** Interview Question)
#Write a method called has_loop that is part of the linked list class.

#The method should be able to detect if there is a cycle or loop present in the linked list.

#The method should utilize Floyd's cycle-finding algorithm, also known as the "tortoise and hare" algorithm, to determine the presence of a loop efficiently.
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return True
    
    def has_loop(self):
        # 1. Initialize two pointers: 'slow' and 'fast', both starting from the head.
        slow=self.head
        fast=self.head

        # 2. Continue traversal as long as the 'fast' pointer and its next node aren't None.
        # This ensure we don't run into errors trying to access non-existent nodes.
        while fast is not None and fast.next is not None:
            # 2.1 Move 'slow' pointer one step ahead
            slow=slow.next
            # 2.2 Move 'fast' pointer two steps ahead.
            fast=fast.next.next
            # 2.3 Check for cycle: If 'slow' and 'fast' meet, it meens there's a cycle in the linked list.
            if(slow==fast):
                # 2.3.1 If they meet, return True indicating the list has a loop
                return True
        # 3. If we've gone through the entire list and the pointers never met,then the list doesn't have a loop
        return False
    
my_linked_list=LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.tail.next=my_linked_list.head
print(my_linked_list.has_loop())


my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop() ) 



# DLL: Reverse ( ** Interview Question)
# Create a new method called reverse that reverses the order of the nodes in the list, i.e., the first node becomes the last node, the second node becomes the second-to-last node, and so on.

# To do this, you'll need to traverse the list and change the direction of the pointers between the nodes so that they point in the opposite direction.

# Do not change the value of any of the nodes.

# Once you've done this for all nodes, you'll also need to update the head and tail pointers to reflect the new order of the nodes.



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
        while temp:
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
    
    def reverse(self):
        if self.head is None or self.head==self.tail:
            return 
        # 1. Initialize 'current_node' to the starting node of the doubly linked list.
        temp=self.head

        #2. Traverse through each node of the doubly linked list.
        while temp:
            # 2.1 Swap the 'next' and 'prev' pointers of the current node.
            # This effectively reverses the direction of the node's pointers.
            temp.prev,temp.next=temp.next,temp.prev
            # 2.2 Since the 'next and 'prev' pointers of the 'current_node' has been swapped, 
            # we move to what was originally the 'prev' node to continue the reversal.
            # Note; In a reversed scenerio,'prev' becomes 'next',hence we use 'prev'.
            temp=temp.prev
        # 3. After all the nodes have been reversed, the original head becomes the tail
            # and the original tail becomes the head.Swap the 'head' and 'tail' of the linked list.
        self.head,self.tail=self.tail,self.head

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)


print('DLL before reverse():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.reverse()


print('\nDLL after reverse():')
my_doubly_linked_list.print_list()

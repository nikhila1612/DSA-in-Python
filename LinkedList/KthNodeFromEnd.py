#LL: Find Kth Node From End ( ** Interview Question)
#Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    
def find_kth_from_end(ll,k):
    # 1. Initialize two pointers,'slow' and 'fast', both pointing to the starting node of the linked list.
    slow=fast=ll.head
    # 2. Move the 'fast' pointer 'k' positions ahead.
    for _ in range(k):
        # 2.1 If at any point during these 'k' movements, the 'fast' pointer reaches the end of the list,then it means the list has less than 'k' nodes,and thus,returning None is appropriate.
        if fast is None:
            return None
        # 2.2. Move the 'fast' pointer to the next node.
        fast=fast.next
    # 3. Now,move both 'slow' and 'fast' pointers one node at a time until the 'fast' pointer reaches the end of the list.Since the 'fast' pointer is already 'k' nodes ahead of the 'slow' pointer,
    #by the time 'fast' reaches the end, 'slow' will be at the kth node from the end.
    while fast is not None:
        slow=slow.next
        fast=fast.next
    # 4. Return the "slow" pointer, which is now pointing to the kth node from the end.
    return slow

my_linked_list=LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

k=4
result = find_kth_from_end(my_linked_list,k)
print(result.value)
  
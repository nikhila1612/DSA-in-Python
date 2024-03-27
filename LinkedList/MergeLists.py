# Definition for singly-linked list.
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def mergeTwoLists(list1,list2):
    # Dummy node to start the merged list
    dummy=ListNode()
    # Pointer to traverse the merged list
    current=dummy

    # Traverse both lists simultaneously
    while list1 and list2:
        # Compare values of nodes from both lists
        if list1.val < list2.val:
            current.next=list1
            list1=list1.next
        else:
            current.next=list2
            list2=list2.next
        # Move the pointer forward in the merged list
        current=current.next
    
    # If any list still has remaining elements, append them to the merged list
    if list1:
        current.next=list1
    if list2:
        current.next=list2
    # Return the head of the merged list (skipping the dummy node)
    return dummy.next

# Helper function to create a linked list from a list of values
def createLinkedList(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next=ListNode(val)
        current=current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linkedListToList(head):
    result=[]
    current=head
    while current:
        result.append(current.val)
        current=current.next
    return result


list1=createLinkedList([1,2,4])
list2=createLinkedList([1,3,4])
merge_list=mergeTwoLists(list1,list2)
print(linkedListToList(merge_list))
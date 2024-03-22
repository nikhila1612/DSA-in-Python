#LL: Binary to Decimal ( ** Interview Question)

#Your task is to implement the binary_to_decimal method for the LinkedList class. This method should convert a binary number, represented as a linked list, to its decimal equivalent.

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.length=1
    
    def append(self,value):
        new_node=Node(value)
        if self.length == 0:
            self.head =new_node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_node
        self.length+=1
    
    def print_list(self):
        if self.head is None:
            print("empty list")
        else:
            temp=self.head
            values=[]
            while temp is not None:
                values.append(str(temp.value))
                temp=temp.next
            print("->".join(values))

    def binary_to_decimal(self):
        # 1. Initialize a variable 'num' to 0.
        # This will be used to accumulate the decimal value as we traverse the linked list.
        num=0
        # 2. Start at the head of the linked list.
        current=self.head
        # 3. Traverse through the linked list.
        while current:
            # 3.1 For each node, left shift the accumulated value by 1 position.
            # This is the same as multiplying by 2. This step ensures that we are
            # moving to the next binary position.
            # 3.2. Add the current node's value (which should be either 0 or 1) 
            # to the accumulated value 'num'.
            num=num*2+current.value
            # 3.3. Move to the next node in the list.
            current=current.next
        # 4. Return the accumulated decimal value.
        return num
            
# Test case 1:Binary number 110 = Decimal number 6
linked_list = LinkedList(1)
linked_list.append(1)
linked_list.append(0)
result =linked_list.binary_to_decimal()
try:
    assert result==6
    print("Test case 1 passed, returned: ",result)
except AssertionError:
    print("Test case 1 failed,returned:c",result)

# Test case 2: Binary number 1000 = Decimal number 8
linked_list = LinkedList(1)
linked_list.append(0)
linked_list.append(0)
linked_list.append(0)
result = linked_list.binary_to_decimal()
try:
    assert result == 8
    print("Test case 2 passed, returned: ", result)
except AssertionError:
    print("Test case 2 failed, returned: ", result)

# Test case 3: Binary number 0 = Decimal number 0
linked_list = LinkedList(0)
result = linked_list.binary_to_decimal()
try:
    assert result == 0
    print("Test case 3 passed, returned: ", result)
except AssertionError:
    print("Test case 3 failed, returned: ", result)

# Test case 4: Binary number 1 = Decimal number 1
linked_list = LinkedList(1)
result = linked_list.binary_to_decimal()
try:
    assert result == 1
    print("Test case 4 passed, returned: ", result)
except AssertionError:
    print("Test case 4 failed, returned: ", result)

# Test case 5: Binary number 1101 = Decimal number 13
linked_list = LinkedList(1)
linked_list.append(1)
linked_list.append(0)
linked_list.append(1)
result = linked_list.binary_to_decimal()
try:
    assert result == 13
    print("Test case 5 passed, returned: ", result)
except AssertionError:
    print("Test case 5 failed, returned: ", result)
    
 
"""
    EXPECTED OUTPUT:
    ----------------
    Test case 1 passed, returned:  6
    Test case 2 passed, returned:  8
    Test case 3 passed, returned:  0
    Test case 4 passed, returned:  1
    Test case 5 passed, returned:  13
"""


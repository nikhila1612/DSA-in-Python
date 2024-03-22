# Define the Node class for a singly linked list
class Node:
    # Constructor for the Node class
    def __init__(self,value):
        # Set the value attribute for the Node
        self.value=value
        # Initialize the next attribute to None
        self.next=None

# Define the LinkedList class
class LinkedList:
    # Constructor for the LinkedList class
    def __init__(self,value):
        # Create a new Node with the given value
        new_node=Node(value)
        # Set the head attribute to the new Node
        self.head=new_node
        # Set the tail attribute to the new Node
        self.tail=new_node
        # Initialize the length attribute to 1
        self.length=1
    
    def print_list(self):
        # Set a temporary pointer(temp) to the head of the list to start traversal
        temp=self.head
        # Iterate through the list until the end (temp is None)
        while temp is not None:
            # Print the value of the current node (temp)
            print(temp.value)
            # Move the temporary pointer (temp) to the next node in the list
            temp=temp.next

    def append(self,value):
        # Create a new Node with the given value
        new_node=Node(value)

        # Check to see if the linked list is empty 
        if self.head is None:
            # Point both head and tail at the new node
            self.head=new_node
            self.tail=new_node
        else:
            # Point the next pointer of the last node at the new node
            self.tail.next=new_node
            # Point tail at the new node
            self.tail=new_node
        # Increment the length of the linked list   
        self.length+=1

     
    def pop(self):
        # Check if the list is empty
        if self.length==0:
            return None
        
        # Initialize temp and pre to the head
        pre=self.head
        temp=self.head

        # Iterate until the last node
        while(temp.next):
            pre=temp
            temp=temp.next
        # Set the new tail to the previous node
        self.tail=pre
        # Remove link to the last node
        self.tail.next=None
        # Decrement list length by 1
        self.length-=1
        
        # Check if the list is now empty
        if self.length==0:
            # Set head and tail to None
            self.tail=None
            self.head=None
        # Return the removed node
        return temp # or use temp.value to return the value of the removed node 
    
    def prepend(self,value):
        # Create new Node with the given value
        new_node=Node(value)
        # Check if the linked list is empty
        if self.length==0:
            # Set the head and tail attributes to the new node
            self.head=new_node
            self.tail=new_node
        else:
            # Set the next attribute of the new node to the current head
            new_node.next=self.head
            # Update the head attribute to the new node
            self.head=new_node

        # Increment the length attribute of the LinkedList    
        self.length+=1
        # Return true to indicate a successful operation
        return True
    
    def pop_first(self):
        # Check if the list is empty
        if self.length==0:
            return None
        # Save a reference to the current head node
        temp=self.head

        # Update the head to the second node in the list
        self.head=self.head.next
        # Disconnect the removed node from the list
        temp.next=None
        # Decrease the length of the list by 1
        self.length-=1
        # Check if the list is now empty
        if self.length==0:
            # Set the tail to None if the list is empty
            self.tail=None
        # Return the removed node
        return temp.value
            
    def get(self,index):
        # Check if the given index is out of bounds or off limits
        if index < 0 or index >= self.length:
            return None
        # Initialize a temporary variable to the head of the list
        temp=self.head
        #Traverse the list 'index' times
        for _ in range(index):
            # Move the temporary variable to the next node in the list
            temp=temp.next
        #Return the node at the specified index
        return temp
    
    def set_value(self,index,value):
        # Call the 'get' method to find the node at the specified index 
        temp= self.get(index)
        # Check if a valid node was found at the specified index
        if temp:
            # Update the value of the found node with the given value
            temp.value =value
            # Return True to indicate that the value was updated successfully 
            return True
        # If no valid node was found, return False to indicate the value was not updated
        return False
    
    def insert(self,index,value):
        # Check if the index is out of bounds
        if index<0 or index>self.length:
            return False
        # If index is 0,prepend the value
        if index==0:
            return self.prepend(value)
        # If index is at the end,append the value
        if index==self.length:
            return self.append(value)
        # Create a new node with the value
        new_node=Node(value)
        # Get the node just before the insertion point
        temp=self.get(index-1)
        # Set new_node's next to temp's next
        new_node.next=temp.next
        # Update temp's next to the new_node
        temp.next=new_node
        # Increment the length of the list
        self.length+=1
        # Return True as node inserted successfully
        return True
    
    def remove(self,index):
        # Check if index is out of bounds
        if index<0 or index>self.length:
            return None
        # Remove and return the first node
        if index==0:
            return self.pop_first()
        # Remove and return the last node
        if index==self.length-1:
            return self.pop()
        # Get the previous node
        pre=self.get(index-1)
        # Set temp to the node to be removed
        temp=pre.next
        # Update pre.next to skip the removed node
        pre.next=temp.next
        # Disconnect the removed node
        temp.next=None
        # Decrement the list length
        self.length-=1
        # Return the removed node
        return temp
    
    def reverse(self):
        # Swap the head and tail pointers
        temp=self.head
        self.head=self.tail
        self.tail=temp
        # Initialize variables for the next and previous nodes
        after=temp.next
        before=None
        # Iterate through the list to reverse the next pointers
        for _ in range(self.length):
            # Store the next node in the list
            after=temp.next
            # Update the current node's next pointer to the previous node
            temp.next=before
            # Move the previous node to the current node
            before= temp
            # Move the current node to the next node in the list
            temp=after


        



my_linked_list=LinkedList(4)
# print(my_linked_list.head.value)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.reverse()
my_linked_list.print_list()
#print(my_linked_list.pop_first())
#print(my_linked_list.pop_first())

#if list has 2 or more items
#print(my_linked_list.pop())
#if list has only 1 item 
#print(my_linked_list.pop())
#if only single item is present
#print(my_linked_list.pop())
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        # Create a new node with the provided value
        new_node=Node(value)
        # Check if the tree is empty
        if self.root is None:
            # Make the new node the root and return True
            self.root = new_node
            return True
        # Start at the root of the tree
        temp = self.root

        # Loop until the correct spot is found
        while (True):
            # Check for duplicate values
            if new_node.value==temp.value:
                # Duplicate found, return False
                return False
            
            # Check if the new value is less than current node's value
            if new_node.value<temp.value:
                # Is the left child spot empty?
                if temp.left is None:
                    # Insert new node as left child , return True
                    temp.left=new_node
                    return True
                # If new value is greater, go to the right child
                temp=temp.left
            else:
                # Is the right child spot empty?
                if temp.right is None:
                    # Insert new node as right child,return True
                    temp.right=new_node
                    return True
                # If not empty, move to right child
                temp=temp.right

    def contains(self,value):
        # Start by setting 'temp' to the root of the tree
        temp=self.root
        # Loop until 'temp' becomes None (end of tree)
        while (temp is not None):
            #If value to find is less than the current node's value
            if value < temp.value:
                # Move 'temp' to the left child and continue loop
                temp=temp.left
            # If value to find is less than the current node's value
            elif value>temp.value:
                # Move 'temp' to the right child and continue loop
                temp=temp.right
            # If value is neither less nor greater, it must be equal
            else:
                # Value found! Return True
                return True
        #If loop ends, vaue was not found in tree. Return False.
        return False

my_tree = BinarySearchTree()
my_tree.insert(3)
my_tree.insert(5)
my_tree.insert(2)
my_tree.insert(27)
my_tree.insert(7)

print(my_tree.contains(27))
print(my_tree.contains(5))


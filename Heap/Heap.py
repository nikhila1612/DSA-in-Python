class MaxHeap:
    def __init__(self):
        self.heap=[]
    
    def _left_child(self,index):
        return 2 * index + 1
    
    def _right_child(self,index):
        return 2 * index + 2
    
    def _parent(self,index):
        return (index-1) // 2
    
    def _swap(self,index1,index2):
        self.heap[index1], self.heap[index2]=self.heap[index2],self.heap[index1]

    def insert(self,value):
        # Add the new value at the end of the heap. This maintains the complete
        # binary tree property of the heap.
        self.heap.append(value)

        # Set 'current' to the index of the newly inserted value. 'current' will
        # be used to track the value as it may move up the heap.
        current=len(self.heap)-1


        # Start a loop that continues until the heap property is restored.
        # The heap property for a max heap states that every parent node must be greater than or 
        # or equal to its child nodes.
        while current > 0 and self.heap[current]> self.heap[self._parent(current)]:
            # If the newly inserted value is greater than its parent,
            # swap them to restore the heap property
            self._swap(current, self._parent(current))
            # Move 'current' to its parent index for the next iteration.
            # This allows the newly inserted value to continue moving up the heap until
            # the heap property is restored.
            current=self._parent(current)

    
    def _sink_down(self,index):
        # Assume that the given 'index' is the index of the maximum value.
        # If it isn't, we will correct this assumption in the loop.
        max_index = index
    
        # Start an infinite loop. We'll break out of this loop manually when the maximum value is at the correct index.
        while True:
            # Compute the indices of the left and right children of 'index'
            left_index= self._left_child(index)
            right_index = self._right_child(index)


            # If the left child exists and is greater than the current max_value,update
            # max_index to left_index.
            if (left_index<len(self.heap) and self.heap[left_index] > self.heap[max_index]):
                max_index = left_index
            # Similarly, if the right child exists and is greater than the current max_value, update max_index to right_index.
            if (right_index<len(self.heap) and self.heap[right_index]> self.heap[max_index]):
                max_index = right_index
            # If the parent node at 'index' is less than either of its children,
            # swap it with the larger child. Otherwise, the heap property has been restored and 
            # we can break out of the loop.
            if max_index!=index:
                self._swap(index,max_index)
                index =max_index # Update 'index' for the next iteration.
            else:
                return # The heap property has been restored.
    
    def remove(self):
        # If heap is empty, return None. There's no value to remove.
        if len(self.heap)==0:
            return None    

        # If only one element is in the heap, pop and return it. After this,
        # the heap will be empty. No need to restructure.
        if len(self.heap)==1:
            return self.heap.pop()
        
        # Save the root value of the heap. In a max heap, the root is always the maximum value.
        max_value=self.heap[0]

        # Remove the last value in the heap and set it as the new root
        # This operation may violate the max heap property, as the new root may be less than its childresn.
        self.heap[0]=self.heap.pop()
        # Filter down the new root. This operation shifts down the new root value to its 
        # proper possition, such that the max heap property is restored.
        self._sink_down(0)

        # Return the maximum value that has been removed. the heap now has the max heap
        # property with the maximum value removed.
        return max_value





myheap = MaxHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)
myheap.insert(100)
myheap.insert(75)

print(myheap.heap)

myheap.remove()

print(myheap.heap)

myheap.remove()


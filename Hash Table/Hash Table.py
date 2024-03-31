class HashTable:
    def __init__(self,size=7):
        # Initialize the hash table with a given size,default is 7
        self.data_map = [None] * size

    # Method to calculate the hash value of a key
    def __hash(self,key):
        my_hash =0
        for letter in key:
            # Calculate hash using a simple algorithm (sum of ASCII values multiplied by 23)
            my_hash = (my_hash + ord(letter)* 23)% len(self.data_map)
        return my_hash
    
    # Method to print the contents of the hash table
    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i,':',val)

    # Method to insert a key-value pair into the hash table
    def set_item(self,key,value):
        # Calculate the index using the hash function
        index=self.__hash(key)
        if self.data_map[index]==None:
            # If the index is empty, initialize it with an empty list
            self.data_map[index]=[]
        # Append the key-value pair to the list at the calculated index
        self.data_map[index].append([key,value])
    
    # Method to get the value of the key
    def get_item(self,key):
        # Calculate the index using the hash function
        index=self.__hash(key)
        # Check if there's any data stored at the calculated index
        if self.data_map[index] is not None:
            # Iterate through list of key-value pairs stored at the index
            for i in range(len(self.data_map[index])):
                # Check if the current key in the list matches the requested key
                if self.data_map[index][i][0]== key:
                    # if the key matches, return the corresponding value
                    return self.data_map[index][i][1]
        # If the key is not found or the index is empty,return None
        return None
    
    def keys(self):
        # Initialize an empty list to store all keys
        all_keys=[]
        # Iterate through each index in the data_map
        for i in range(len(self.data_map)):
            # Check if there is data stored at the current index
            if self.data_map[i] is not None:
                # Iterate through each key-value pair stored at the current index
                for j in range(len(self.data_map[i])):
                    # Append the key from the current key-value pair to all_keys list
                    all_keys.append(self.data_map[i][j][0])
        # Return the list containing all keys
        return all_keys
my_hash_table = HashTable()

my_hash_table.set_item('bolts',1400)
my_hash_table.set_item('washers',50)

print(my_hash_table.get_item('bolts'))
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('lumber'))

print(my_hash_table.keys())
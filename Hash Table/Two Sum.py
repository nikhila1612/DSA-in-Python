# HT: Two Sum ( ** Interview Question)
# two_sum()

# Problem:
# Given an array of integers nums and a target integer target, find the indices of two numbers in the array that add up to the target.

# The main challenge here is to implement this function in one pass through the array. This means you should not iterate over the array more than once. Therefore, your solution should have a time complexity of O(n), where n is the number of elements in nums.



# Input:

# A list of integers nums .

# A target integer target.



# Output:

# A list of two integers representing the indices of the two numbers in the input array nums that add up to the target. If no two numbers in the input array add up to the target, return an empty list [].


def two_sum(nums,target):
    nums_map={}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in nums_map:
            return [nums_map[complement],i]
        nums_map[num]=i
    return []

print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))  
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
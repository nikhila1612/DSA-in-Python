# Set: Find Pairs ( ** Interview Question)
# You are given two lists of integers, arr1 and arr2, and a target integer value, target. Your task is to find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.

# Write a function called find_pairs that takes in three arguments: arr1, arr2, and target, and returns a list of all such pairs.  Assume that each array does not contain duplicate values.

# Input

# Your function should take in the following inputs:

# arr1: a list of integers

# arr2: a list of integers

# target: an integer


# Output

# Your function should return a list of tuples, where each tuple contains two integers from arr1 and arr2 that add up to target.

def find_pairs(arr1,arr2,target):
    set1=set(arr1)
    pairs=[]
    for i in arr2:
        complement=target-i
        if complement in set1:
            pairs.append((complement,i))
    return pairs

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)
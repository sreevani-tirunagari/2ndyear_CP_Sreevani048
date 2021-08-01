"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
     
    # search space is `A[left…right]`
    (left, right) = (0, len(input_array) - 1)
 
    # loop till the search space is exhausted
    while left <= right:
 
        # find the mid-value in the search space and
        # compares it with the target
 
        mid = (left + right) // 2
 
        # overflow can happen. Use:
        # mid = left + (right - left) / 2
        # mid = right - (right - left) // 2
 
        # key is found
        if value == input_array[mid]:
            return mid
 
        # discard all elements in the right search space,
        # including the middle element
        elif value < input_array[mid]:
            right = mid - 1
 
        # discard all elements in the left search space,
        # including the middle element
        else:
            left = mid + 1
 
    # `x` doesn't exist in the list
    return -1

# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    middle = int((end+start) // 2)
    if arr[middle] == target:
        return middle
    elif target > arr[middle]:
        binary_search(arr, target, start=middle, last=last)
    elif target < arr[middle]:
        binary_search(arr, target, start=start, last=middle)
    if start == last:
        return

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here


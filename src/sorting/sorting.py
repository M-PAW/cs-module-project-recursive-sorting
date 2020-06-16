# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    curr_idx = elements
    merge_idx = 0
    while curr_idx > 0:
        for i in arrA:
            merge_arr[merge_idx] = arrA[i]
            merge_idx +=1
        for j in arrB:
            merge_arr[merge_idx] = arrB[j]
            merge_idx += 1


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        return merger(merge_sort(left), merge_sort(right))

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here


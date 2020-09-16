# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    a = 0
    b = 0
    count = 0
    merged_arr = [0] * elements
    # Your code here
    while a < len(arrA) or b < len(arrB):
        print(count)
        if a >= len(arrA):
            merged_arr[count] = arrB[b]
            b += 1 
        elif b >= len(arrB):
            merged_arr[count] = arrA[a]
            a += 1  
        elif arrA[a] > arrB[b]:
            merged_arr[count] = arrB[b]
            b += 1
        else:
            merged_arr[count] = arrA[a]
            a += 1
        count += 1    
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        midpoint = len(arr) // 2
        leftArr = arr[:midpoint]
        left = merge_sort(leftArr)
        rightArr= arr[midpoint:]
        right = merge_sort(rightArr)
        return merge(left, right)
    
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here
    # Index for input arrays
    index = 0
    # Index for return array
    indexM = 0

    # Since we are cutting the input array one by one 
    # We can check while length of those arrays
    while len(arrA) > 0 and len(arrB) > 0:

        # if arrayA smaller than arrayB
        if arrA[index] < arrB[index]:
            # Put that array into return array
            merged_arr[indexM] = arrA[index]
            indexM += 1
            # Cut the input array
            arrA = arrA[1:]

        # elif arrayA bigger than arrayB
        elif arrA[index] >= arrB[index]: 
            # Put that array into return array                      
            merged_arr[indexM] = arrB[index]
            indexM += 1
            # Cut the input array
            arrB = arrB[1:]

    # If one array is empty, and the other still have some arrays
    # We do the same thing as above
    while len(arrA) > 0 or len(arrB) > 0:
        if len(arrA) > 0:
            merged_arr[indexM] = arrA[index]
            indexM += 1
            arrA = arrA[1:]
        elif len(arrB) > 0:
            merged_arr[indexM] = arrB[index]
            indexM += 1
            arrB = arrB[1:]

    return merged_arr

print(merge([1],[2]))
# # TO-DO: implement the Merge Sort function below recursively
# def merge_sort(arr):
#     # Your code here


#     return arr

# # STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists 
# # or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here


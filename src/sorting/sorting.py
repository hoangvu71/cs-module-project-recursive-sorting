# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here
    index = 0
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[index] < arrB[index]:
            for indexM in range(len(merged_arr)):
                if merged_arr[indexM] == 0:
                    merged_arr[indexM] = arrA[index]
                    arrA = arrA[1:]                        
                    break
        elif arrA[index] >= arrB[index]:
            for indexM in merged_arr:
                if merged_arr[indexM] == 0:                        
                    merged_arr[indexM] = arrB[index]
                    arrB = arrB[1:]
                    break
    while len(arrA) > 0 or len(arrB) > 0:
        if len(arrA) > 0:
            for indexM in range(len(merged_arr)):
                if merged_arr[indexM] == 0:
                    merged_arr[indexM] = arrA[index]
                    arrA = arrA[1:]
                    break            
        elif len(arrB) > 0:
                if merged_arr[indexM] == 0:
                    merged_arr[indexM] = arrB[index]
                    arrB = arrB[1:]
                    break
    return merged_arr

print(merge([1,3,5,9,11,19],[2,4,6,7,8,12]))
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


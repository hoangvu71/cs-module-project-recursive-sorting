# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    tree_root_index = (end + start) // 2
    if len(arr) == 0: 
        return -1
    if target == arr[tree_root_index]:
        print("Found it ")
        return tree_root_index
    # If target is larger than tree root
    else:
        if target > arr[tree_root_index]:
            return binary_search(arr, target, tree_root_index + 1, len(arr) - 1)
    
    # Elif target is smaller than tree root
        if target <= arr[tree_root_index]:
            return binary_search(arr, target, start, tree_root_index + 1)

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search(arr1, -8, 0, len(arr1)-1))

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass


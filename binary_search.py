def binary_search(arr, target):
    # initialize left and right pointers
    left = 0
    right = len(arr) - 1

    # continue searching while left pointer is less than or equal to right pointer
    while left <= right:
        # calculate middle index and value
        mid = (left + right) // 2
        mid_val = arr[mid]

        # if target is found, return the index
        if mid_val == target:
            return mid

        # if target is less than the middle value, search the left half of the array
        elif target < mid_val:
            right = mid - 1

        # if target is greater than the middle value, search the right half of the array
        else:
            left = mid + 1

    # if target is not found, return -1
    return -1
# define an example array and target value
arr = [1, 3, 5, 7, 9]
target = 7

# perform a binary search for the target value in the array
result = binary_search(arr, target)

# print the result
if result != -1:
    print("Target found at index",result)
else:
    print("Target not found in array")
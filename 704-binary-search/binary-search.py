def binary_search(nums, target):
    # initialize 2 pointers
    start = 0
    end = len(nums)

    while start < end:
        mid = start + (end-start) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid
        else:
            start = mid + 1

    # if we reach here, means target was not found in the array
    return -1

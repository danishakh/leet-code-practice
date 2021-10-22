def searchInsert(nums, target):
    if len(nums) == 0:
        return 0

    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return start


# [1, 2, 3, 5, 7, 8, 9]
# search for 6

# 1. start = 0, nums[start] = 1
# end = 6, mid = 0 + (6-0)/2 = 3
# nums[3] = 5, 5 < 6 -> start = 3+1= 4

# 2. start = 4, nums[start] = 7
# end = 6, mid = 4 + (6-4)/2 = 5
# nums[5] = 8, 8 > 6 -> end = 4

# 3. start = 4, nums[start] = 7;
# end = 4, mid = 4 + (4-4)/2 = 4
# nums[4] = 7, 7 > 6 -> end = 3

# start < end -> FALSE
# insert at index 4!


# [1, 2, 3, 5, 7, 8, 9] - search for 4

# 1. start = 0
# end = 6, mid = 0 + (6-0)/2 = 3
# nums[3] = 5, 5 > 4 -> end = 3-1 = 2
#
# 2. start = 0
# end = 2, mid = 0 + (2-0)/2 = 1
# nums[1] = 2, 2 < 4 -> start = 1 + 1= 2
#
# 3. start = 2
# end = 2, mid = 2 + (2 - 2) /2 = 2
# nums[2] = 3, 3 < 4 -> start = 2 + 1 = 3

# 4. start = 3, end = 2 -------> break
# return start = 3
# insert at index 3!

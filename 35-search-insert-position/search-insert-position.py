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
# end = 5, mid = 4 + (5-4)/2 = 4
# nums[4] = 7, 7 > 6 -> end = 3

# start < end -> FALSE
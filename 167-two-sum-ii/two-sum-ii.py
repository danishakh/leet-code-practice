def two_sum_ii(nums, target):
    # since the array is sorted, our task is easier
    # 2 pointer approach

    left = 0
    right = len(nums)-1

    while left <= right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left+1, right+1]    # +1 bec look at example... weird

# Space: O(1)
# Time: O(N)

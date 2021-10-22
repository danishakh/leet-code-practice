def rotate_arr(nums, k):
    # when it comes to rotating, think about reversing the array

    # in-case k > len(nums)
    k = k % len(nums)

    # 1. reverse the whole array
    left = 0
    right = len(nums)-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    # 2. reverse the 1st k elements
    left = 0
    right = k-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    # 3. reverse the remaining elements
    left = k
    right = len(nums)-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

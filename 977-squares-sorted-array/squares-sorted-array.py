def squaresSortedArray(nums):
    # create a results array of same size as nums
    res = [0]*len(nums)

    # 2 pointer approach
    left = 0;
    right = len(nums)-1

    # pointer to insert in new array
    resultsIdx = len(nums)-1

    while left <= right:
        if nums[left]*nums[left] >= nums[right]*nums[right]:
            res[resultsIdx] = nums[left]*nums[left]
            left +=1 
        else:
            res[resultsIdx] = nums[right]*nums[right]
            right -= 1
        resultsIdx -= 1
    
    return res
# generic binary search - pass in left and right edges of array 
def binary_search(left, right, direction):
    while left <= right:
        mid = left + (right - left) // 2
        # we will get the direction as an argument from another 
        # function, and move in that direction accordingly
        result = direction(mid)

        if result == 'found':
            return mid
        elif result == 'left':
            right = mid - 1
        else:
            left = mid + 1
    return -1

# find the left most index of target 
def starting_pos(nums, target):
    def find_direction(mid):
        if nums[mid] == target:
            # this line!
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, find_direction)

# find the right most index of target
def ending_pos(nums, target):
    def find_direction(mid):
        if nums[mid] == target:
            # this line!
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, find_direction)

def start_and_end(nums, target):
    return starting_pos(nums, target), ending_pos(nums, target)
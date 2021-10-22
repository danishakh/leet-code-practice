def reverse_str(arr):
    left = 0
    right = len(arr)-1

    while left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


print(reverse_str(['d', 'y', 'b', 'a', 'l', 'a']))

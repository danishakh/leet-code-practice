def move_zeroes(arr):
    # 2 pointer approach
    a = 0
    b = 0

    for b in range(len(arr)):
        if arr[b] != 0:
            arr[a], arr[b] = arr[b], arr[a]
            a += 1
    return arr


print(move_zeroes([0, 1, 2, 0, 3, 0, 0, 0, 6, 10]))


# another 2 pointer approach
def move_zeroes_2(arr):
    # count number of 0s
    zero_counter = arr.count(0)

    # pointer for next non-0 number to be inserted
    a = 0

    # move all the non-0s to the start of the array
    for n in arr:
        if n != 0:
            arr[a] = n
            a += 1

    # insert the counted amount of 0s from the right
    for i in range(1, zero_counter+1):
        arr[-i] = 0

    return arr


print(move_zeroes_2([1, 2, 0, 0, 4, 0, 5, 7]))

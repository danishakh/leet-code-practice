# this problem is an extension of binary search

# BETTER solution
def firstBadVersion2(n):
    if n < 2:
        return n

    start = 1
    end = n
    res = 0

    while start <= end:
        mid = start + (end - start) // 2

        if isBadVersion(mid):
            res = mid
            end = mid - 1
        else:
            start = mid + 1

    # res will eventually end up at the 1st bad version position
    return res


def firstBadVersion(n):
    if n < 2:
        return n

    start = 1
    end = n

    while start <= end:
        mid = start + (end - start) // 2

        if isBadVersion(mid) and not isBadVersion(mid-1):
            return mid

        # 1st bad version is to the left of mid
        elif isBadVersion(mid) and isBadVersion(mid-1):
            end = mid - 1

        # not isBadVersion(mid) - 1st bad version is to the right of mid
        else:
            start = mid + 1

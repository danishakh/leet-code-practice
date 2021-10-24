# BETTER solution - hare/tortoise approach
def middleNode(head):
    # 2 pointer approach
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    return slow


# brute force?
def middleNode2(head):
    start = head
    len_list = 0
    
    # count length of linked list / number of nodes
    while start:
        len_list += 1
        start = start.next
    
    mid = len_list // 2

    start2 = head
    count = 0

    while start2:
        if count == mid:
            return start2
        else:
            count += 1
            start2 = start2.next

    
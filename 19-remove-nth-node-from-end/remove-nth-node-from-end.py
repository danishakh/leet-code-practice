# 2 pointer approach
# BETTER
def removeNth(head, n):
    first = second = head
    # move first pointer by n positions
    for i in range(n):
        first = first.next
    
    # if first is null, then we need to remove head
    if not first:
        return head.next
    
    # keep iterating until first.next == null
    while first.next:
        first = first.next
        second = second.next
    # at this point, second is pointing at the node we want to remove
    second.next = second.next.next

    return head




# Brute Force? 
def removeNth2(head, n):
    start = head
    len_list = 0
    while start:
        len_list += 1
        start = start.next

    # need to change idxNodeToChange's next pointer
    idxNodeToChange = len_list - n

    count = 1
    start2 = head

    if idxNodeToChange > 0:
        while count < idxNodeToChange:
            start2 = start2.next
            count += 1

        start2.next = start2.next.next
    # idxNodeToChange = 0 -> means remove head
    else:
        return head.next
    
    return head
    
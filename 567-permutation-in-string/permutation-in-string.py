import collections

def checkInclusion(s1, s2) -> bool:
    s1_len = len(s1)
    s2_len = len(s2)

    # base case checks
    if s1_len > s2_len or s2_len == 0:
        return False
    if s1_len == 0:
        return True
    
    # initialize array to keep track of freq of each letter
    arr = [0]*26

    # increment val by 1 for letters in s1
    for s in s1:
        arr[ord(s) - ord('a')] += 1

    # decrement val by 1 for 1st len(s1) letters in s2
    for s in range(s1_len):
        arr[ord(s2[s]) - ord('a')] -= 1
    
    match = True
    # check if all vals are = 0
    for i in arr:
        if i != 0:
            match = False
            break
    
    if match: return True

    # as long as there are atleast len(s1) letters in s2, for each window starting at i:
    for i in range(1, s2_len - s1_len + 1):
        # get index of left letter removed from window by sliding right
        idxLetterLeft = ord(s2[i-1]) - ord('a')
        # get index of right letter added to window by sliding right
        idxLetterRight = ord(s2[i + s1_len - 1]) - ord('a')

        arr[idxLetterLeft] += 1
        arr[idxLetterRight] -= 1

        # check for all 0s again
        match = True
        for i in arr:
            if i != 0:
                match = False
                break
        
        if match: return True
    
    return False


# another solution - easier to type in python due to Counter
# although much slower to execute on larger strings than solution above
def checkInclusion2(s1: str, s2: str) -> bool:
        # creates a dictionary of counts of each element in string
        s1_counter = collections.Counter(s1)
        
        s1_len = len(s1)
        s2_len = len(s2)
        
        for i in range(s2_len - s1_len + 1):
            # creates a dictionary for window of len(s1) elements in s2, and compare
            if collections.Counter(s2[i:i+s1_len]) == s1_counter:
                return True
            
        return False
def lengthOfLongestSubstr(s):
    seen = {}
    res = 0
    # sliding window - window is between i and j
    left = 0

    for right in range(len(s)):
        # check if letter exists in dict
        if s[right] in seen:
            # move left pointer of i to previous index of repeated char 
            # IF its inside window, else just keep i as it is
            i = max(i, seen[s[right]] + 1)
        
        # update dictionary with latest index of letter
        seen[s[right]] = right

        # update res
        res = max(res, right - left + 1)
    return res;
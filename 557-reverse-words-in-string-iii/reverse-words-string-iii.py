def reverseWords(s):
    res = []
    s_arr = s.split(' ')
    
    for word in s_arr:
        # change the word to a list
        char_arr = list(word)

        # 2 pointer approach
        i = 0
        j = len(char_arr)-1
        
        # swap values
        while i < j:
            char_arr[i], char_arr[j] = char_arr[j], char_arr[i]
            i +=1
            j -=1
        # append the reversed word into results array
        res.append(''.join(char_arr))
    
    return ' '.join(res)


# Better solution using python slicing
def reverseWords2(s):
    # initialize results array
    res = []
    arr = s.split(' ')

    for word in arr:
        # python slicing
        new = word[::-1]
        res.append(new)
    
    return ' '.join(res)
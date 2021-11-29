def validParenthesis(str1):
    # there has to be an even number of characters in the str
    if len(str1) % 2 != 0:
        return False

    stack = []
    # having this makes the code simpler
    closeToOpen = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    for s in str1:
        # if s is one of the keys in closeToOpen
        if s in closeToOpen:
            # check if the stack is empty and the last element is the 'opposite' of s
            if stack and stack[-1] == closeToOpen[s]:
                stack.pop()
            else:
                return False
        else:
            # if s is not one of the keys, then push it to the stack
            stack.append(s)
    
    # stack should be empty at this point, if its not then not a valid parenthesis
    return not stack





s1 = '({})()()'
s2 = '({)}'
s3 = '(){}[][[]]({})'
s4 = '"([}}])"'
print(validParenthesis(s1))
print(validParenthesis(s2))
print(validParenthesis(s3))
print(validParenthesis(s4))
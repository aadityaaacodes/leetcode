def isValid(s: str):
    closing = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    checker = []

    for i in s:
        if i in closing:
            if (len(checker) > 0) and (checker[-1]==closing[i]):
                checker.pop()
            else:
                return False
        else:
            checker.append(i)
    
    if len(checker) == 0:
        return True
    else:
        return False
    
print(isValid("()"))
def func(haystack = "leetcode", needle = "leeto"):
    ind = 0 
    temp = ""
    for i in range(0, len(haystack)):
        if haystack[i] == needle[0]:
            ind = i
            for j in range(i, i+len(needle)):
                temp += haystack[j]
            if temp == needle:
                print(temp)
                return(ind)
            else:
                temp = ""
    else:
        return(-1)

print(func())
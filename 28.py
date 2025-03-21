def func(haystack = "sadbutsad", needle = "sad"):
    try:
        return(haystack.index(needle))
    except:
        return(-1)
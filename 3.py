def func(st):
    n = len(st)
    ret_li = []
    for i in range(n):
        c = st[i]
        try:    
            a = i
            b = st.index(c, a+1)
        except:
            b = n

        if not b == n or b == n:
            ret_li.append(st[a:b])

    return(ret_li)

s = "pwwkew"
li = func(s)
print(max(li))

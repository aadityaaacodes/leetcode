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

li = func(st= "pwwkew")
li2 = []
for i in li:
    li2.append(func(i))

for j in li2:
    print(j)

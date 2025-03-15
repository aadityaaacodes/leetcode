strs = ["ab", "a"]
n = len(strs)
pre = ""
pre = strs[0]

ch = []
k = 0
flag = True

# print(strs[0][5])

# if n == 1:
#     flag = False


for i in strs:
    if len(i) == 0:
        flag = False

while flag:
    for i in strs:
        a = i[k]
        if a == pre[k]:
            ch.append(a)
        
    if len(ch) == n: #all elements in ch are the same
        if k == len(pre)-1: #all elements in strs are the same
            flag = False
        else:
            k = k + 1
            ch.clear()
    else:
        pre = pre[0:k]
        flag = False

if k == 0 and n>1: #nothing is similar
    pre = ""

print(pre, k)




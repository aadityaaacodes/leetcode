words1 = ["rsvyxfkbmllnsvfmiskouagjpymub","xqadhorgvguprqp"]
words2 = ["rsvyxfkbmllnsvfmiskouagjpymub","xqadhorgvguprqp","wvtjffkonflbmdmw","olekom","tcnrpyshlqvsisnk","jqwigwkehsvyylrixvbmrq","irrjybaruytqixlozgtb","ebsxabicklczdjoqahxybuvav","k","hoayhbdmxipzqxkkarjcfszgaolxo"]
li = []
for i in words1:
    for j in words2:
        if i == j and not i in li:
            li.append(j)
# print(li)

count = {}
for a in li:
    count.update({a:0})

c = 0
for k in words1:
    if k in li:
        c +=1+count[k]
        count.update({k:c})
    c = 0
# print(count)

c = 0 
for l in words2:
    if l in li:
        c +=1+count[l]
        count.update({l:c})
    c = 0
num=0
for m in li:
    if count[m] == 2:
        num +=1

print(num)











# count = {}
# c = 0
# print(li)






# print(count)

# for m in words2:
#     if m in li:
#         c+=1
#     count.update({m:c})
#     c = 0

# print(count)
# num = 0
# for n in li:
#     if count[n] == 1:
#         num+=1

# print(num)

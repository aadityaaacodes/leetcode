digits = "23"
map = {
    2 : ['a', 'b', 'c'],
    3 : ['d', 'e', 'f'], 
    4 : ['g', 'h', 'i'], 
    5 : ['j', 'k', 'l'], 
    6 : ['m', 'n', 'o'], 
    7 : ['p', 'q', 'r', 's'], 
    8 : ['t', 'u', 'v'], 
    9 : ['w', 'x', 'y', 'z']
}

ind = [] # to store digits
for i in digits: 
    if not i == "": 
        ind.append(int(i))

# print(ind)

cmb = [] # to store combinations

for i in ind:
    cmb.append(map[i])

pd = []
n=0
while n > len(cmb):
    for i in range(len(cmb)):
        for j in range(i):
            print(cmb[n][j])
    n=n+1

print(cmb)
# ot[0][0]

# print[pd]










# if ind == []:
#     ot = []
# else:
#     for k in map[ind[0]]: 
#         for l in map[ind[1]]:
#             ot.append(f"{k}{l}")




# print(ot)

# print(map[ind[0]])




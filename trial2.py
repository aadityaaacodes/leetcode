digits = "234"

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

cmb = [] # holds combinations
for i in digits: 
    if not i == "": 
        cmb.append(map[int(i)])

n = len(cmb)

# print(cmb)

op = []
temp = []


for i in cmb[0]:
    temp.append(i)

# print(temp)

# for k in range(len(temp)):

for i in cmb[1]:
    print(i)
        # temp[k] = f"{temp[k]} {i}"

print(temp)




# for i in cmb:
#     print(i[2])





# print(cmb)
s = "abcdefghij"
k = 3
fill = "x"

li = []
c = int(len(s)%k)

if not (c == 0):
    for m in range(0, k-c):
        s += fill

print(s)
n = int(len(s)/k)

for i in range(0, n):
    li.append(s[(i*k):(i*k)+k])

# if (c == 0):
#     for i in range(0, n):
#         li.append(s[(i*k):(i*k)+k])
# else:
#     for i in range(0, n):
#         li.append(s[(i*k):(i*k)+k])

print(li)
# n = int(len(s) / 3)
# cond = len(s) % 3
# li = []
# a = 0
# for i in range(0, n):
#     print(s[a:i+k])
#     a = i+k-1
#         # print(i)



# print(n)
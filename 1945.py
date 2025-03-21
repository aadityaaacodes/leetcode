s = "leetcode"
k = 2
sum = 0
convert = ""
for i in s:
    convert += str(ord(i) - 96)

for r in range(0, k):
    for j in convert:
        sum += int(j)
    convert = str(sum)
    sum = 0

# print(sum)
print(int(convert))
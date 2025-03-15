# n = 1000
# sum = 0
# for i in range(1, n+1, 1):
#     sum+=(1.0/i)

# sum2 = 0
# for j in range(n+1, 1, -1):
#     sum2+= (1.0/j)

# print(sum, sum2)



a = 0
b = 0
temp = 0
sum = 0
n = 3

for i in range(n):
    sum = a + b
    print(sum, a, b)
    temp = b
    b = a + b
    a = temp

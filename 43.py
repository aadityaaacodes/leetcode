num1 = "0"
num2 = "0"

n1 = 0
c = len(num1)-1
for i in range(0, len(num1)):
    n1 += ((ord(num1[i])-48) * (10**c))
    c -=1

n2 = 0
c = len(num2)-1
for i in range(0, len(num2)):
    n2 += ((ord(num2[i])-48) * (10**c))
    c -=1

product = n1*n2
# print(product)
st = ""
e = 0 

while product>=0:
    e = product % 10
    product = (product // 10)
    st = chr(e+48) + st
    if product == 0:
        break


print(st)
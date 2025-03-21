n = 15
li = []
for i in range(1, n+1):
    if i % 3 == 0:
        if i % 5 == 0:
            li.append("FizzBuzz")
        else:
            li.append("Fizz")
    else:
        if  i % 5 == 0:
            li.append("Buzz")
        else:
            li.append(str(i))

print(li)
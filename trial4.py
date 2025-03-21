s = "([)]"

a = s.index('(')
if (b = s.index(')')):
    s = s[a+1:b]
print(s)
s = "luffy is still joyboy"
if not s[-1] == ' ':
    s += ' '
a = 0
li = []
temp = ""
for i in range(0, len(s)):
    if s[i] == ' ':
        temp = s[a:i]
        temp = temp.strip()
        if len(temp) > 0 :
            li.append(temp)
        a = i
print((li[-1]))

# print(len(s[a+1:len(s)]))
# in progess

s = "IceCreAm"

l_vowels = ['a', 'e', 'i', 'o', 'u']
u_vowels = ['A', 'E', 'I', 'O', 'U']
ind = []
li = []
for i in range(0, len(s)):
    if s[i] in l_vowels or s[i] in u_vowels:
        ind.append(i)
        li.append(s[i])

print(ind)
print(li)


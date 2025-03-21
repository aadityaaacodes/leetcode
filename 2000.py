word = "abcd"
ch = "z"
ind = -1
for i in range(0, len(word)):
    if word[i] == ch:
        ind = i
        break
if ind == -1:
    print(word)
else:
    s1 = word[0:ind+1]
    s2 = word[ind+1: len(word)]
    rev = ""
    for k in s1:
        rev = k + rev
    word = rev + s2
    print(word)
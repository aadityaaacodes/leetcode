trans = {
    'I': 1,
    'IV':4,
    'V': 5,
    'IX':9,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

s = 'III'
n = len(s)
val = 0
st = ""

c = []

for i in range(len(s)):
    
    if not abs(n-i) > 1:
        if s[i-1]=='I' or s[i+1]=='I':
            c.append()
    
    
    c.append(s[i])

print(val)
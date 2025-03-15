s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
li = s.split(' ')
n = len(li)
new_li = []
flag = True

for i in li:
    try: 
        new_li.append(int(i))
    except:
        continue

print(new_li)

for k in range(len(new_li)):
    for l in range(k):
        if new_li[k] <= new_li[l]:
            flag = False

if flag:
    print('true')
else:
    print('false')
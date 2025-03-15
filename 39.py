target = 8
candidates = [2, 3, 5]
n = len(candidates)
res = []

def dfs(i, temp, sum):
    global target
    
    # base case
    if sum == target:
        res.append(temp.copy())
        return

    if i >= n or sum>target:
        return
    
    temp.append(candidates[i])

    # add element
    dfs(i, temp, sum+candidates[i])

    # don't use element
    temp.pop()
    dfs(i+1, temp, sum)


dfs(i=0, temp=[], sum=0)
print(res)
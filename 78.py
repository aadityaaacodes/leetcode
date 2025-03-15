nums = [1, 2, 3]
n = len(nums)
res, sol = [], []

def backtrack(i):
    # recursive sol added to the final sol
    if i == n:
        res.append(sol[:])
        return
    
    # Don't pick nums
    backtrack(i+1)


    # Pick nums
    sol.append(nums[i]) #adding to temp sol list
    backtrack(i+1) #backtracking with next index
    sol.pop() #popping to make list consistent

(backtrack(0))
print(res)
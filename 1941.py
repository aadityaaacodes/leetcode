class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        sum = 0
        c = []
        for i in s:
            if not i in c:
                c.append(i)
                for j in s:
                    if i == j:
                        sum = sum + 1

        
        if sum%len(c)==0:
            return(True)
        else:
            return(False)
        
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:     
        def subproblem(count, i1, i2):
            if i1 == len(s) or i2 == len(t):
                return count
                
            if s[i1] == t[i2]:
                count += 1
                return subproblem(count, i1+1, i2+1)
            else:
                return subproblem(count, i1, i2+1)
        

        count = subproblem(0, 0, 0)
  
        return count == len(s)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def iterative_subproblem():
            memo = {}
            for i1 in range(len(text1), -1, -1):
                for i2 in range(len(text2), -1, -1):
                    if len(text1[i1:]) == 0 or len(text2[i2:]) == 0:
                        memo[(i1, i2)] = 0
                    elif text1[i1] == text2[i2]:
                        memo[(i1,i2)] = 1 + memo[(i1+1, i2+1)]
                    else:
                        memo[(i1,i2)] = max(memo[(i1+1,i2)], memo[(i1, i2+1)])
            
            return memo[(0,0)]

        memo = {}
        def recursive_subproblem(i1, i2):
            if (i1,i2) not in memo:
                if len(text1[i1:]) == 0 or len(text2[i2:]) == 0:
                    memo[(i1,i2)] = 0
                elif (text1[i1] == text2[i2]):
                    memo[(i1,i2)] = 1 + recursive_subproblem(i1 +1 , i2 + 1)
                else:
                    memo[(i1,i2)] = max(recursive_subproblem(i1+1, i2), recursive_subproblem(i1, i2+1))
            return memo[(i1,i2)]
        
        return iterative_subproblem()
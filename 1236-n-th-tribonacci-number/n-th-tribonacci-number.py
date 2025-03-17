class Solution:
    def tribonacci(self, n: int) -> int:
        return self.dp_iterative(n)
        return self.dp_rec(n, {})

    def dp_rec(self, n: int, memo: dict) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1

        if n not in memo:
            memo[n] =  self.dp_rec(n-1, memo) + self.dp_rec(n-2, memo) + self.dp_rec(n-3, memo)
        
        return memo[n]

    def dp_iterative(self, n: int) -> int:
        memo = {}

        # base cases
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1

        for i in range(3, n+1):
            if i not in memo:
                memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

        return memo[n]
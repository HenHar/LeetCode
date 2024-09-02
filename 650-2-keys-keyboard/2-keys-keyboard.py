class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        return 1 + self.dp(n, 1, 1) # copy to clipboard is always the first step

    def dp(self, n, current, clipboard):
        if current > n:
            return sys.maxsize
        if current == n:
            return 0

        # just paste (1 step)
        opt1 = 1 + self.dp(n, current + clipboard, clipboard)
        # copy and paste (2 steps)
        opt2 = 2 + self.dp(n, current * 2, current)
        
        return min(opt1, opt2)

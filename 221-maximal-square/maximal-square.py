class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        dp = [[0]*(cols+1) for i in range(rows+1)]
        
        max_edge = 0
        for r in range(1, rows+1):
            for c in range(1, cols+1):
                if matrix[r-1][c-1] == "1":
                    dp[r][c] = 1 + min(dp[r-1][c], dp[r-1][c-1], dp[r][c-1])
                    max_edge = max(dp[r][c], max_edge)

        print(dp)
        return max_edge * max_edge
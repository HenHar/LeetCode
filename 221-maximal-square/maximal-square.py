class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        dp = [ [0]*(cols+1) for i in range(rows+1)]
        if matrix[rows-1][cols-1] == "1":
            dp[rows-1][cols-1] = 1
        
        max_edge = 0
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if matrix[r][c] == "1":
                    edge = 1 + min(dp[r+1][c], dp[r+1][c+1], dp[r][c+1])
                    dp[r][c] = edge
                    if edge > max_edge:
                        max_edge = edge

        return max_edge * max_edge
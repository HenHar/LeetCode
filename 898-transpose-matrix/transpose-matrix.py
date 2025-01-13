class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        transposed = [[None for r in range(rows)] for c in range(cols)]
        for r in range(len(matrix)):
            for c in range(0, len(matrix[0])):
                transposed[c][r] = matrix[r][c]
        return transposed
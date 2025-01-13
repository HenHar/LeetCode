class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reverse(matrix)
        return matrix

    def transpose(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            for c in range(r, cols): # only upper matrix
                value = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = value

    def reverse(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            for c in range(0,cols//2): # just go to half of the col for swapping
                reverse_col = cols - 1 - c
                value = matrix[r][c]
                matrix[r][c] = matrix[r][reverse_col]
                matrix[r][reverse_col] = value
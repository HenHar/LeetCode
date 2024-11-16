from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        return self.bfs_iterative(image, sr, sc, color)
        return self.dfs_start(image, sr, sc, color)
        
    def dfs_start(self, image, sr, sc, color):
        if image[sr][sc] == color:
            return image
        startColor = image[sr][sc]
        num_rows = len(image)
        num_cols = len(image[0])
        self.dfs_recursive(image, sr, sc, num_rows, num_cols, startColor, color)
        return image

    def dfs_recursive(self, image, row, col, num_rows, num_cols, startColor, assignColor):
        if row < 0 or row >= num_rows or col < 0 or col >= num_cols:
            return
        if image[row][col] != startColor:
            return

        image[row][col] = assignColor
        self.dfs_recursive(image, row+1, col, num_rows, num_cols, startColor, assignColor)
        self.dfs_recursive(image, row-1, col, num_rows, num_cols, startColor, assignColor)
        self.dfs_recursive(image, row, col+1, num_rows, num_cols, startColor, assignColor)
        self.dfs_recursive(image, row, col-1, num_rows, num_cols, startColor, assignColor)


    def bfs_iterative(self, image: List[List[int]], sr: int, sc: int, color: int):
        q = deque()
        startColor = image[sr][sc]
        num_rows = len(image)
        num_cols = len(image[0])
        if image[sr][sc] != color:
            q.append((sr, sc))

        while q:
            row, col = q.popleft()
            image[row][col] = color
            directions = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for r, c in directions:
                if r >= 0 and r < num_rows and c >= 0 and c < num_cols:
                    if image[r][c] == startColor:
                        q.append((r,c))

        return image
class Solution:
    rows, cols = 0,0

    def bfs(self, grid, r, c):
        q = collections.deque()
        grid[r][c] = "0"
        q.append((r,c))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if r in range(self.rows) and c in range(self.cols) and grid[r][c] == "1":
                    grid[r][c] = "0"
                    q.append((r,c))

    def dfs_recursive(self, grid, r, c):
        if r < 0 or r >= self.rows or c < 0 or c >= self.cols:
            return

        if grid[r][c] == "1":
            grid[r][c] = "0"
            self.dfs_recursive(grid, r-1, c)
            self.dfs_recursive(grid, r+1, c)
            self.dfs_recursive(grid, r, c-1)
            self.dfs_recursive(grid, r, c+1)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows, self.cols = len(grid), len(grid[0])
  
        islands = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == "1":
                    self.dfs_recursive(grid, r, c)
                    islands += 1
            
        return islands

      
        
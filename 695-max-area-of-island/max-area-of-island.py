class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        max_area_island = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    max_area_island = max(max_area_island, self.getIslandArea_andRemoveIsland(grid, row, col, num_rows, num_cols))

        return max_area_island

    def getIslandArea_andRemoveIsland(self, grid, row, col, num_rows, num_cols):
        q = deque()
        q.append((row, col))
        area = 0
        while q:
            r, c = q.popleft()
            area += 1
            grid[r][c] = 0
            directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for r, c in directions:
                if r >= 0 and r < num_rows and c >= 0 and c < num_cols:
                    if grid[r][c] == 1:
                        if (r, c) not in q:
                            q.append((r, c))
        return area

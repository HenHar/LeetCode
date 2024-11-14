class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        max_perimter_per_land = 4
        total_perimeter = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    total_perimeter += max_perimter_per_land - self.get_num_neighbors(row, col, num_rows, num_cols, grid)

        return total_perimeter

    def get_num_neighbors(self, row, col, num_rows, num_cols, grid) -> int:
        neighbors = [(row + 1, col) , (row - 1, col), (row, col + 1), (row, col - 1)]

        num_neighbors = 0
        for r, c in neighbors:
            if r >= 0 and r < num_rows and c >= 0 and c < num_cols:
                if grid[r][c] == 1:
                    num_neighbors += 1
        return num_neighbors


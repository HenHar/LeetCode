class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        def getMax(x: int, y: int, grid: List[List[int]]) -> int:
            maxValue = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    if grid[y+j][x+i] > maxValue:
                        maxValue = grid[y+j][x+i]
            return maxValue

        n_size = len(grid) - 2
        max_grid = list([0 for x in range(n_size)] for y in range(n_size))
    
        for x in range(n_size):
            for y in range(n_size):
                max_grid[x][y] = getMax(y+1,x+1, grid)

        return max_grid
import numpy as np

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check9Numbers(nums: List[str]) -> bool:
            nums = list(int(x) for x in nums if x != ".")
            if len(set(nums)) == len(nums):
                return True
            return False

        # check rows
        for row in board:
            if not check9Numbers(row): 
                return False

        # check columns
        for col in zip(*board):
            if not check9Numbers(col): 
                return False

        # check subboxes
        for i in (0,3,6):
            for j in (0,3,6):
                nums = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                if not check9Numbers(nums): 
                    return False
        return True
    
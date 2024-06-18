class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        start = 0
        end = m*n

        while start <= end:
            mid = (start + end) // 2 
            mid_r, mid_c = mid // n, mid % n

            if mid_r < m and mid_c < n:
                mid_value = matrix[mid_r][mid_c]
     
            if target > mid_value:
                start = mid + 1
            elif target < mid_value:
                end = mid - 1
            else:
                return True

        return False
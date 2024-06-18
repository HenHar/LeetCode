class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        start = 0
        end = len(height) - 1
        distance = end - start


        while (distance != 0):
            max_area = max(max_area, distance * min(height[start], height[end]))

            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
            distance = end - start
        
        return max_area


        
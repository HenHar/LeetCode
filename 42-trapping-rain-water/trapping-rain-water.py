class Solution:
    def trap(self, height: List[int]) -> int:
        num_items = len(height)
        total_trapped_water = 0
        max_height = max(height)
        index_max_value = height.index(max(height))

        left_max = 0
        for l in range(0, index_max_value):
            curr_height = height[l]
            left_max = max(curr_height, left_max)
            trapped_water = max(0, left_max - curr_height)
            total_trapped_water += trapped_water
        
        right_max = 0
        for r in range(num_items - 1, index_max_value, -1):
            curr_height = height[r]
            right_max = max(curr_height, right_max)
            trapped_water = max(0, right_max - curr_height)
            total_trapped_water += trapped_water
        
        return total_trapped_water
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.greedy(nums)

    def greedy(self, nums):
        farthest_index = 0
        for i in range(len(nums) - 1):
            if i > farthest_index:
                return False
                
            farthest_index =  max(farthest_index, i + nums[i])

        return farthest_index >= len(nums) - 1

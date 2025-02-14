class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.greedy(nums)

    def greedy(self, nums):
        furthest_index = 0
        for i in range(len(nums) - 1):
            if i <= furthest_index:
                furthest_index =  max(furthest_index, i + nums[i])

        return furthest_index >= len(nums) - 1

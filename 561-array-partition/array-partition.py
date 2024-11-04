class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        total_sum = 0
        for i in range(0, len(nums), 2): # after sorting the min is the first item of pairing
            total_sum += nums[i]
        return total_sum
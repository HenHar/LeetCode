class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = {}
        for i in nums:
            counter[i] = counter.get(i, 0) + 1

        nums = set(nums)
        nums = sorted(nums)

        earnings = [0] * len(nums)
        for i in range(len(nums)):
            value = nums[i]
            not_take = 0
            take = value * counter[value]
            if i-1 >= 0 and value - nums[i-1] != 1:
                take += earnings[i-1]
            elif i-2 >= 0:
                take += earnings[i-2]
            
            if i-1 >= 0:
                not_take += earnings[i-1]
            earnings[i] = max(take, not_take)

        return earnings[-1]



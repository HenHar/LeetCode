class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets =  []
        self.recSubsets(nums, list(), subsets)
        return subsets

    def recSubsets(self, nums, subset, subsets):
        if len(nums) == 0:
            subsets.append(subset)
            return

        value = nums.pop(0)
        self.recSubsets(nums.copy(), subset.copy() + [value], subsets)
        self.recSubsets(nums.copy(), subset.copy(), subsets)
            
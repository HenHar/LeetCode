class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #return self.xor_solution(nums)
        return self.hash_table_solution(nums)

    def hash_table_solution(self, nums):
        hash_table = {i: False for i in range(len(nums) + 1)}
        for i in nums:
            hash_table[i] = True

        for i in range(len(nums) + 1):
            if hash_table[i] == False:
                return i

    def xor_solution(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)):
            res += (i - nums[i])

        return res + i + 1



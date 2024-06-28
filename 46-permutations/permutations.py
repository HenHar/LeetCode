class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(permutation, nums):
            if len(nums) == 0:
                permutations.append(permutation.copy())
                return

            for i in nums.copy():
                nums.remove(i)
                backtracking(permutation + [i], nums.copy())
                nums.append(i)

        permutations = []
        backtracking([], nums)
        return permutations
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_frequency_map = {}

        for num in nums:
            num_frequency_map[num] = 1 + num_frequency_map.get(num, 0)

        max_subsequence_count = 0
        for num, frequency in num_frequency_map.items():
            if num + 1 in num_frequency_map:
                total_count = frequency + num_frequency_map[num + 1]
                max_subsequence_count = max(max_subsequence_count, total_count)

        return max_subsequence_count
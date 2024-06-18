class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = {}
        for i in nums:
            countNums[i] = countNums.get(i, 0) + 1
        sortedDict = sorted(countNums, key = countNums.get)
        return sortedDict[-k:]
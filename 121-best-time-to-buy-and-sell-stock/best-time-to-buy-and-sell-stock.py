class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max = 0
        for p in prices[1:]:
            if p < min:
                min = p

            if p - min > max:
                max = p - min

        return max
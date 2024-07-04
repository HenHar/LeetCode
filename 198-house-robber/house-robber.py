class Solution:
    """
    M(k): money in kth house
    DP(0) = 0
    P(1) = M(1)
    DP(k) = max(DP(k-1), M(k) + DP(k-2))
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * (n + 1)

        for i in range(0, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return max(dp[-2],dp[-1])

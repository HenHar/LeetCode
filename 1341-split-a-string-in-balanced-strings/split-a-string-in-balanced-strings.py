class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num_substrings = 0
        numR, numL = 0, 0
        for ch in s:
            if ch == "R":
                numR += 1
            else:
                numL += 1
            if numR == numL:
                num_substrings += 1
                numR, numL = 0, 0
        return num_substrings
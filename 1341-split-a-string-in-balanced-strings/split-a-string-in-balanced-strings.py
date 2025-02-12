class Solution:
    def balancedStringSplit(self, s: str) -> int:
        substrings = 0
        balanced = 0
        for ch in s:
            if ch == "R":
                balanced += 1
            else:
                balanced -= 1
            if balanced == 0:
                substrings += 1
        return substrings
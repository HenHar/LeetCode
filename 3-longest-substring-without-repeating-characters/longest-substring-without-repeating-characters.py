class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = 0
        substring = ""
        for c in s:
            index = substring.find(c)
            if index == -1:
                substring += c
                max_substring = max(len(substring), max_substring)
            else:
                substring += c
                substring = substring[index + 1:]

        return max_substring

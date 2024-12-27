class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        frequency_map = {}
        count = 0
        min_substring_index = 0
        len_min_substring = sys.maxsize
        
        # get character count of t
        for char in t:
            frequency_map[char] = frequency_map.get(char, 0) + 1

        while right < len(s):
            # check occurence of charcter in hash map, increment count by one if character present
            if s[right] in frequency_map:
                frequency_map[s[right]] -= 1
                if frequency_map[s[right]] >= 0:
                    count += 1
            # valid solution if all characters are present in substring
            while count == len(t):
                # update solution
                if right - left + 1 < len_min_substring:
                    min_substring_index = left
                    len_min_substring = right - left + 1
                # shrink window from left, decrement character frequency of hash map 
                if s[left] in frequency_map:
                    frequency_map[s[left]] += 1
                    if frequency_map[s[left]] > 0:
                        count -= 1
                left += 1
            right += 1

        if len_min_substring == sys.maxsize:
            len_min_substring = 0
        end_index = min_substring_index + len_min_substring
        return s[min_substring_index:end_index]
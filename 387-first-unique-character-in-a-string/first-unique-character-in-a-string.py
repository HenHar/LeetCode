class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter_map = {}

        for char in s:
            counter_map[char] = counter_map.get(char, 0) + 1

        for index, char in enumerate(s):
            if counter_map[char] == 1:
                return index
        
        return -1


        
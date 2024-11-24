class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        character_count = {}
        maxSubString = 0
        
        # dynamic sliding window -> grow to right
        windowStart = 0
        for windowEnd in range(len(s)):
            currChar = s[windowEnd]
            character_count[currChar] = 1 + character_count.get(currChar, 0)
            num_characters_to_change =  self.getNumberOfCharactersToChange(windowStart, windowEnd, character_count)

            # condition not fullfied -> shrink window from left
            while (num_characters_to_change > k):
                currChar = s[windowStart]
                character_count[currChar] -= 1
                windowStart += 1
                num_characters_to_change =  self.getNumberOfCharactersToChange(windowStart, windowEnd, character_count)
            
            # update max value
            length_substring = (windowEnd + 1) - windowStart
            maxSubString = max(maxSubString, length_substring)

        return maxSubString

    def getNumberOfCharactersToChange(self, windowStart : int,  windowEnd : int, character_count: dict) -> int:
        length_substring = (windowEnd + 1) - windowStart
        max_occurence_character = max(character_count.values())
        return length_substring - max_occurence_character
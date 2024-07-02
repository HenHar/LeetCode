class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
            
        mapping = { "1" : [],
                    "2" : ['a', 'b', 'c'],
                    "3" : ['d', 'e', 'f'],
                    "4" : ['g', 'h', 'i'],
                    "5" : ['j', 'k', 'l'],
                    "6" : ['m', 'n', 'o'],
                    "7" : ['p', 'q', 'r', 's'],
                    "8" : ['t', 'u', 'v'],
                    "9" : ['w', 'x', 'y', 'z']
                    }
        combinations = []
        def backtracking(combination, digits):
            if len(digits) == 0:
                combinations.append(combination)
                return

            digit = digits[0]
            for char in mapping[digit]:
                backtracking(combination + char, digits[1:])

        backtracking(str(), digits)
        
        return combinations

        
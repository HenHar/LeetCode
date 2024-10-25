class Solution:
    def romanToInt(self, s: str) -> int:
        romanToInt_map = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        total_sum = 0
        last_roman_value = 0
        
        for c in reversed(s):
            summand = romanToInt_map[c]
            if romanToInt_map[c] < last_roman_value:
                summand = -summand

            total_sum += summand
            last_roman_value = romanToInt_map[c]

        return total_sum
        


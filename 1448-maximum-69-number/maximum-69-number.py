class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = str(num)
        new_digits = ""
        first6 = True
        for digit in digits:
            if digit == "6" and first6:
                first6 = False
                digit = "9"
            
            new_digits += digit

        return int(new_digits)
                
        
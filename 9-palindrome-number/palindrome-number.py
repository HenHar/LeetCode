class Solution:
    def reverseNum(self, num: int) -> int:
        revNum = 0
        while num > 0:
           revNum = (revNum * 10) + (num % 10)
           num = num // 10

        return revNum

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            if self.reverseNum(x) - x == 0:
                return True
            else:
                return False

 


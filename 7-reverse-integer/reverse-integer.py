class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = -x

        revNum = 0

        while x > 0:
            a = x % 10
            revNum = revNum * 10 + a
            x = x // 10


        if abs(revNum) < 2**31 and revNum != 2**31 - 1:
            return sign * revNum
        else:
            return 0
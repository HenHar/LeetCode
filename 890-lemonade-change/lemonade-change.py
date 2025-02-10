class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0
        count10 = 0
        for pay in bills:
            if pay == 5:
                count5 += 1     

            if pay == 10:
                count5 -= 1
                count10 += 1

            if pay == 20:
                if count10 >= 1 and count5 >= 1:
                   count10 -= 1
                   count5 -= 1
                else:
                    count5 -= 3
            
            if count5 < 0:
                return False
                
        return True
            
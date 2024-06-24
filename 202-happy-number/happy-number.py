class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0
        seenSums = set()
        while (sum != 1):
            sum = 0
            while (n != 0):
                sum += ((n % 10)**2) 
                n = (n//10)

            if sum == 1:
                return True
            if sum in seenSums:
                return False
            else:
                seenSums.add(sum)

            n = sum
    
           
            


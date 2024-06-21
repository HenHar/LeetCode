class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid
            
            if hours <= h:
                r = mid - 1
            else:
                l = mid + 1

        return l


        

import math

class Solution_firsttry:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)

        k = 1
        rate = 2
        while(rate > 1.0):
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k

            rate = hours/h
            k = rate*k
            if k > max_pile:
                k = max_pile
                break
            print("k: ", k, " rate: ", rate, " hours: ", hours)
        
        print(max_pile, k)
                
        return math.ceil(k)


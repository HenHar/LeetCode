class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        collected = []
        for pay in bills:
            current = pay
            while True:
                if current == 5:
                    collected.append(pay)
                    break
                if current > 20 and 20 in collected:
                    current -= 20
                    collected.remove(20)
                elif current > 10 and 10 in collected:
                    current -= 10
                    collected.remove(10)
                elif current > 5 and 5 in collected:
                    current -= 5
                    collected.remove(5)
                else:
                    return False                    
        
        return True
            
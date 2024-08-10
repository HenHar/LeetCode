class Solution:
    def divisorGame(self, n: int) -> bool:
        return self.dp(n, True)

    def dp(self, n, alices_turn):
        if n == 1:
            return not alices_turn
        if n == 2:
            return alices_turn

        for x in range(1, n):
            if n % x == 0:
                return self.dp(n -x,  not alices_turn) 
            else:
                return not alices_turn

        
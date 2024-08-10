class Solution:
    def divisorGame(self, n: int) -> bool:
        return self.dp_iterative(n)

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

    def dp_iterative(self, n):
        alice_turns = False
        x = 1
        while x < n:
            if n % x == 0:
                n = n-x
            else:
                x += 1
            alice_turns = not alice_turns

        return alice_turns 
        
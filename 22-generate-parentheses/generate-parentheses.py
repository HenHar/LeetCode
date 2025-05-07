class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp_combinations = [[] for i in range(n+1)]
        dp_combinations[0].append("")
        dp_combinations[1].append("()")

        for i in range(2, n+1):
            unique = set()
            for combinations in dp_combinations[i-1]:
                for i2 in range(len(combinations)):
                    new_combination = combinations[:i2] + "()" + combinations[i2:]
                    unique.add(new_combination)
            dp_combinations[i] = list(unique)

        return dp_combinations[n]
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(combination, candidates, target):
            #print(target, combination, candidates)
            if len(candidates) < 1:
                return
            
            # follow right path with removed first canidate and no change in node value
            dfs(combination.copy(), candidates[1:].copy(), target)

            value = candidates[0]
            if target - value == 0:
                #print("#", target, value, combination)
                combination.append(value)
                combinations.append(combination)
                return

            if target - value < 0:
                return
            # follow left path with same candidates and substraction of value
            dfs(combination + [value], candidates.copy(), target - value)
            
            
        combinations = []
        dfs([], candidates, target)

        return combinations

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temp_list = []
        
        for i, temp in enumerate(reversed(temperatures)):
            
            while len(stack) > 0 and temp >= stack[-1][1] :
                stack.pop()

            if (len(stack) == 0):
                temp_list.append(0)
            else:
                temp_list.append(-(stack[-1][0] - i))

            stack.append((i, temp))

        return reversed(temp_list)
        
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for t in tokens:
            if t in operators:
                b = stack.pop()
                a = stack.pop()

                result = eval(a + t + b)
                stack.append(str(int(result)))
            else:
                stack.append(t)

           
        return eval(stack[-1])
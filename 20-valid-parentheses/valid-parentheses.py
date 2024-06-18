class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")" : "(",
                    "]" : "[",         
                    "}" : "{"}
        stack = []

        for br in s:
            if br in brackets.values():
                stack.append(br)   
            elif not stack or not stack.pop() == brackets[br]:
                return False
   
        return not stack
            
                
                

     


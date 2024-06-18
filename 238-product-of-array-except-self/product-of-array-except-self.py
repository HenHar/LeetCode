import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        prod = 1
        for i in nums:
            left.append(prod)
            prod *= i
            

        right = []
        prod = 1
        for i in reversed(nums):
            right.append(prod)
            prod *= i
            
        prod_list = []
        right = list(x for x in reversed(right))
        for i in range(len(nums)):
            prod_list.append(left[i]*right[i])
        
        return prod_list
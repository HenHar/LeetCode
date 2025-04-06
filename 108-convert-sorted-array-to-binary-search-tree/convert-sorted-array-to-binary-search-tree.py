# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.buildBST(nums)
        


    def buildBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        middle = len(nums) // 2
        left = self.buildBST(nums[0:middle])
        right = self.buildBST(nums[middle+1:])
        node = TreeNode(nums[middle], left, right)

        return node


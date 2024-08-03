# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.traverseTree(root, -1000000)

    def traverseTree(self, root, maxValue) -> int:
        current = 0
 
        if root:
            if root.val >= maxValue:
                current = 1
                maxValue = root.val

            return current + self.traverseTree(root.left, maxValue) +  self.traverseTree(root.right, maxValue)
            
        return current
        
      
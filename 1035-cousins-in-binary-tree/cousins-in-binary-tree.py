# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        result = []
        self.dfs(root, result, x, y, 0, root)
        
        if len(result) != 2:
            return False

        depth1, parent1 = result[0]
        depth2, parent2 = result[1]
        
        return depth1 == depth2 and parent1 != parent2

    def dfs(self, root, result, x, y, depth, parent):
        if not root:
            return
 
        if root.val == x:
            result.append((depth, parent.val))
        if root.val == y:
            result.append((depth, parent.val))

        self.dfs(root.left, result, x, y, depth+1, root)
        self.dfs(root.right, result, x, y, depth+1, root)
        
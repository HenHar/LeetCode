from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs_iterative(root, targetSum)
        return self.dfs_recursive(root, 0, targetSum)

    def dfs_recursive(self, root: Optional[TreeNode], path_sum: int, targetSum: int) -> bool:
        if not root:
            return False

        path_sum += root.val
        if not root.left and not root.right:
            if path_sum == targetSum:
                return True
        left = self.dfs_recursive(root.left, path_sum, targetSum)
        right = self.dfs_recursive(root.right, path_sum, targetSum)

        return left or right

    def dfs_iterative(self, root, targetSum):
        if not root:
            return False

        stack = deque()
        stack.append((root, root.val))
        while stack:
            node, path_sum = stack.pop()
            if not node.left and not node.right:
                if path_sum == targetSum:
                    return True

            if node.right:
                stack.append((node.right, path_sum + node.right.val))
            if node.left:
                stack.append((node.left, path_sum + node.left.val))

        return False
        
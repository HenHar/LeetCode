# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.recInvert(root)

        return root


    def recInvert(self, node):
        if node:
            left = node.left
            node.left = node.right
            node.right = left

            if node.left:
                self.recInvert(node.left)

            if node.right:
                self.recInvert(node.right)

        
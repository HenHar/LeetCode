# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        order = []
        self.inOrderTraversal(root, order)

        return order[k-1]

    def inOrderTraversal(self, root, order):
        # go left
        if root.left:
            self.inOrderTraversal(root.left, order)
        # take root
        order.append(root.val)
        # go right
        if root.right:
            self.inOrderTraversal(root.right, order)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        #self.recursion(root, preorder)
        preorder = self.iterative(root)
        return preorder

    def iterative(self, root):
        preorder = []
        if not root:
            return preorder

        q = deque()
        q.append(root)

        while q:
            node = q.pop()
            preorder.append(node.val)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)

        return preorder

    def recursion(self, root, preorder):
        if not root:
            return
        
        preorder.append(root.val)
        if root.left:
            self.recursion(root.left, preorder)
        if root.right:
            self.recursion(root.right, preorder)
    
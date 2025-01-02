from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #return self.bfs_iterative(root)
        return self.bfs_recursive(root)

    def bfs_recursive(self, root):
        result = []
        if root:
            self.bfs_recursive_call(root, result, 0)
        return result

    def bfs_recursive_call(self, node, result, level):
        if level > len(result) - 1:
                result.append([])

        result[level].append(node.val)

        if node.left:
            self.bfs_recursive_call(node.left, result, level+1)
        if node.right:
            self.bfs_recursive_call(node.right, result, level+1)


    def bfs_iterative(self, root):
        q = deque()
        result = []
        level = 0
        if root:
            q.append((root,level))
        
        while q:
            current_node, level = q.popleft()
            if level > len(result) - 1:
                result.append([])
            result[level].append(current_node.val)
            
            if current_node.left:
                q.append((current_node.left, level + 1))
            if current_node.right:
                q.append((current_node.right, level + 1))

        return result
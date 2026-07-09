# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_diam = [0]
        
        def dfs(node):

            if not node:
                return 0
            
            left_h = dfs(node.left)
            right_h = dfs(node.right)

            diam = left_h + right_h
            max_diam[0] = max(max_diam[0], diam)

            return 1 + max(left_h, right_h)
        
        dfs(root)

        return max_diam[0]

        return max

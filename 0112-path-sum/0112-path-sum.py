# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:

        
        def dfs(node, target):

            if not node:
                return False

            target = target - node.val

            if target == 0 and not node.left and not node.right:
                return True
            

            left = dfs(node.left, target)
            right = dfs(node.right, target)

            return left or right
        
        return dfs(root, targetSum)
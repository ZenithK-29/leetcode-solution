# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxValue):

            if not node:
                return 0

            res = 1 if node.val >= maxValue else 0

            maxValue = max(node.val, maxValue)

            left = dfs(node.left, maxValue)
            right = dfs(node.right, maxValue)

            res += left + right

            return res

        return dfs(root, root.val)

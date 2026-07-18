# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        #iterative soln

        curr = root

        while curr:

            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
            
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
            else:
                return curr

        # #recursive soln
        # if not root:
        #     return None
        
        # if root == p or root == q:
        #     return root
        
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # if left is not None and right is not None:
        #     return root
        
        # if left is not None and right is None:
        #     return left

        # return right

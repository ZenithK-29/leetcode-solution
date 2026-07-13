# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


        #iterative soln

        n = 0
        curr = root
        stack = []

        while curr or stack:

            while curr: #add all leftmode nodes into stack for inorder traversal
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()  #pop the topmost element of stack after we hit null

            n+=1  #nth smallest element

            if n == k: #if nth smalles  = kth smallest
                return curr.val
            
            curr = curr.right #go to right node
        
        #recursive soln
        # count = [0]
        # def inorder_dfs(node):

        #     if not node:
        #         return 
            
        #     left = inorder_dfs(node.left)

        #     if left:
        #         return left
            
        #     count[0] +=1
        #     if count[0] == k:
        #         return node
            

        #     right = inorder_dfs(node.right)

        #     if right:
        #         return right
            
        #     return None
        
        # return inorder_dfs(root).val

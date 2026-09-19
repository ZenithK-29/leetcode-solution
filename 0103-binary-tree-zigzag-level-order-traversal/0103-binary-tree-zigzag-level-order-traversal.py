# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:

        if not root:
            return []
        
        zig = 0
        q = deque()
        q.append(root)
        res = []

        while q:

            qLen = len(q)
            lvl = []
            for i in range(qLen):

                node = q.popleft()
                lvl.append(node.val)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            if zig %2 != 0:
                lvl.reverse()

            zig +=1

            if lvl:    
                res.append(lvl)
        
        return res
                    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        q = deque()
        q.append(root)

        res = [[root.val]]
        level = 0

        while q:

            qLen = len(q)
            temp = []

            for i in range(qLen):

                node = q.popleft()

                if node.left:
                    q.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    temp.append(node.right.val)
                
            if temp:

                if level % 2 == 0:
                    res.append(temp[::-1])
                else:
                    res.append(temp)

            level +=1

        return res
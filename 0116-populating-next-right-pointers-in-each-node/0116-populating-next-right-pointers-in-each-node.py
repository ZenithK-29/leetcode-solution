"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        curr, next_lvl = root, root.left if root else None

        while curr and next_lvl:

            curr.left.next = curr.right #connect siblings

            if curr.next:
                curr.right.next = curr.next.left # connect children from different parents

            curr = curr.next

            if curr is None: #has no more neighbor nodes horizontally
                curr = next_lvl #moves to a level down
                next_lvl = curr.left
        
        return root
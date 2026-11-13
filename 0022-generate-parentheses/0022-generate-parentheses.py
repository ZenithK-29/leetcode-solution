class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        res = []
        
        def helper(open, closing, temp):

            if open == n and closing == n:
                res.append("".join(temp))
                return
            
            if open < n:
                temp.append("(")
                helper(open+1, closing, temp)
                temp.pop()
            
            if closing < open:
                temp.append(")")
                helper(open, closing+1, temp)
                temp.pop()
        
        helper(0, 0, [])

        return res

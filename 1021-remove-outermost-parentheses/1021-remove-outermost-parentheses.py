class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        

        #optmized soln without stack

        depth = 0 #this replaced the stack size. 
        res = ""

        for br in s:

            if br == "(":

                if depth > 0: #this is just equivalent of is stack empty
                    res += br

                depth+=1

            else:

                depth -=1

                if depth > 0: #this is just equivalent of is stack empty
                    res += br
        
        return res


        

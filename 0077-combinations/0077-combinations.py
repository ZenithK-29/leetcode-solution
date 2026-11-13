class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        
        res = []

        def helper(lim, temp):

            if len(temp) == k:
                res.append(temp[:])
                return
            
            if lim > n:
                return
            
            helper(lim+1, temp)

            temp.append(lim)
            helper(lim+1, temp)

            temp.pop()
        
        helper(1, [])

        return res
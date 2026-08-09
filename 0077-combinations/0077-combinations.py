class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        def dfs(start, k, temp):

            if k == 0:
                res.append(temp[:])
                return
            
            if start > n:
                return

            temp.append(start)
            dfs(start+1, k-1, temp)

            temp.pop()
            dfs(start+1, k, temp)
        
        dfs(1, k, [])

        return res
    

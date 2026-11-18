class Solution:
    def climbStairs(self, n: int) -> int:

        #Tabular soln

        dp = [0] * (n+1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1] 


        #memoized soln
        # dp = {}
        
        # def dfs(i):

        #     if i == n:
        #         return 1
            
        #     if i > n:
        #         return 0

        #     if i in dp:
        #         return dp[i]

        #     dp[i] = dfs(i+1) + dfs(i+2)
            
        #     return dp[i]

        # return dfs(0)
    

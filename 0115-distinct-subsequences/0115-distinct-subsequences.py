class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        #Tabular DP Soln

        n1, n2 = len(s), len(t)

        dp = [[0] * (n2+1) for _ in range(n1+1)]

        dp[0][0] = 1

        for i in range(1, n1):
            dp[i][0] = 1

        for j in range(1, n2):
            dp[0][j] = 0
        
        for i in range(1, n1+1):

            for j in range(1, n2+1):

                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n1][n2]
        
        



        #Memoized SOLN
        # cache = {}

        # def dfs(i, j):

        #     if j == len(t):
        #         return 1
        #     if i == len(s):
        #         return 0
            
        #     if (i, j) in cache:
        #         return cache[(i, j)]
            
        #     if s[i] == t[j]:
        #         cache[(i, j)] = dfs(i+1, j+1) + dfs(i+1, j)
            
        #     else:
        #         cache[(i, j)] = dfs(i+1, j)
            
        #     return cache[(i, j)]
        
        # return dfs(0, 0)
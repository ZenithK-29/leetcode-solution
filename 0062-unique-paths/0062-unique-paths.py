class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        #Bottom up
        dp =[[0] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1
        
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):

                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
        
        # return grid[m-1][n-1]

        #Top down memoized
        # cache = {}
        # def dfs(row, col):

        #     if row == m-1 and col == n-1:
        #         return 1
            
        #     if (row, col) in cache:
        #         return cache[(row, col)]
            
        #     down = 0
        #     right = 0

        #     if row >= 0 and row+1 < m:
        #         down = dfs(row+1, col)
    
            
        #     if col >= 0 and col+1 < n:
        #         right = dfs(row, col+1)
            
        #     cache[(row, col)] = down+right
        

        #     return cache[(row, col)]
        
        # return dfs(0, 0)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        #Bottom up
        # grid = [[0] * n for _ in range(m)]

        # for i in range(m):

        #     for j in range(n):

        #         if i == 0 or j == 0:
        #             grid[i][j] = 1
                
        #         else:
        #             grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        # return grid[m-1][n-1]

        #Top down memoized
        cache = {}
        def dfs(row, col):

            if row == m-1 and col == n-1:
                return 1
            
            if (row, col) in cache:
                return cache[(row, col)]
            
            down = 0
            right = 0

            if row >= 0 and row+1 < m:
                down = dfs(row+1, col)
    
            
            if col >= 0 and col+1 < n:
                right = dfs(row, col+1)
            
            cache[(row, col)] = down+right
        

            return cache[(row, col)]
        
        return dfs(0, 0)
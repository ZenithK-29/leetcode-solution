class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        #Bottom up approach
        row = len(coins) + 1
        col = amount + 1

        dp = [[0] * (col) for _ in range(row)]

        for i in range(row):
            dp[i][0] = 1
        
        for i in range(1, row):

            for j in range(1, col):

                if j-coins[i-1] >= 0:
                    dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
                
                else:
                    dp[i][j] = dp[i-1][j]
    
        return dp[row-1][col-1]

        
        #Top down approach
        # cache = {}

        # def dfs(i, target):

        #     if target == 0:
        #         return 1
            
        #     if target < 0:
        #         return 0
            
        #     if (i, target) in cache:
        #         return cache[(i, target)]
            
        #     if i == len(coins) and target != 0:
        #         return 0
            
        #     no_of_ways = dfs(i, target - coins[i]) + dfs(i+1, target)
        #     cache[(i, target)] = no_of_ways

        #     return cache[(i, target)]
        # return dfs(0, amount)
            
            

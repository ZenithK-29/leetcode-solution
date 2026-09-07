class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        #Bottom up approach
        n = len(coins)
        dp = [[0] * (amount+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(1, n+1):

            for j in range(1, amount+1):

                if j >= coins[i-1]:

                    dp[i][j] = dp[i][j - coins[i-1]] + dp[i-1][j]
                
                else:

                    dp[i][j] = dp[i-1][j]
        
        return dp[n][amount]

        
        #Top down approach
        # @cache
        # def dfs(i, left):

        #     if i >= len(coins) or left <= 0:
        #         return 1 if left == 0 else 0
            
        #     return dfs(i, left-coins[i]) + dfs(i+1, left)
        
        # return dfs(0, amount)
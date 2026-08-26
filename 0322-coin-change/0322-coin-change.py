class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        #BOTTOM UP Approach

        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for a in range(1,amount+1):

            for c in coins:

                if a-c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])

        return dp[amount] if dp[amount] != float("inf") else -1




        # #TOP DOWN APPRACH
        # memo = {}
        # def dfs(left):

        #     if left == 0:
        #         return 0
        
        #     if left < 0:
        #         return float("inf")
        
        #     if left in memo:
        #         return memo[left]

        #     ans = float("inf")
        
        #     for coin in coins:
        #         ans =min (ans, 1+dfs(left-coin))
        
        #     memo[left] = ans
        #     return ans
    
        # res = dfs(amount)

        # return -1 if res == float("inf") else res
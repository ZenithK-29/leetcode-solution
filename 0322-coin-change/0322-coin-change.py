class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def dfs(left):

            if left == 0:
                return 0
        
            if left < 0:
                return float("inf")
        
            if left in memo:
                return memo[left]

            ans = float("inf")
        
            for coin in coins:
                ans =min (ans, 1+dfs(left-coin))
        
            memo[left] = ans
            return ans
    
        res = dfs(amount)

        return -1 if res == float("inf") else res
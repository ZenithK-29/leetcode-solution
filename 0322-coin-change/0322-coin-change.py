class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(left):

            if left == 0:
                return 0
            
            if left < 0:
                return float("inf")
            
            ans = float("inf")

            for coin in coins:
                ans = min(ans, 1+dfs(left-coin))
            
            return ans
        
        res = dfs(amount)

        return -1 if res==float("inf") else res
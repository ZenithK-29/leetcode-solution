class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        #Top down approach
        @cache
        def dfs(i, left):

            if i >= len(coins) or left <= 0:
                return 1 if left == 0 else 0
            
            return dfs(i, left-coins[i]) + dfs(i+1, left)
        
        return dfs(0, amount)
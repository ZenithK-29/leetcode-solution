class Solution:
    def rob(self, nums: list[int]) -> int:

        dp = {}
        
        def dfs(i, free):

            if i == len(nums):
                return 0

            if (i, free) in dp:
                return dp[(i, free)]
            
            if free == 0:
                return dfs(i+1, 1)
            
            houseToRob = nums[i] + dfs(i+1, 0)
            houseToSkip = dfs(i+1, 1)

            dp[(i, free)] = max(houseToRob, houseToSkip)

            return dp[(i, free)]
        
        return dfs(0, 1)
class Solution:
    def rob(self, nums: list[int]) -> int:

        #Tabular soln

        if len(nums) < 2:
            return nums[0]

        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return dp[-1]



        #MEMOIZED SOLN
        # dp = {}
        
        # def dfs(i, free):

        #     if i == len(nums):
        #         return 0

        #     if (i, free) in dp:
        #         return dp[(i, free)]
            
        #     if free == 0:
        #         return dfs(i+1, 1)
            
        #     houseToRob = nums[i] + dfs(i+1, 0)
        #     houseToSkip = dfs(i+1, 1)

        #     dp[(i, free)] = max(houseToRob, houseToSkip)

        #     return dp[(i, free)]
        
        # return dfs(0, 1)
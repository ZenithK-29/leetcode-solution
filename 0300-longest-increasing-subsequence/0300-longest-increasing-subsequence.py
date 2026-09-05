class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)

        dp =[1] * n

        for i in range(1, n):

            for j in range(0, i):

                if nums[i] > nums[j]:

                    dp[i] = max(dp[j] + 1, dp[i])
        

        maxIndex = 0
        for i in range(n):
            if dp[i] > dp[maxIndex]:
                maxIndex = i
        
        return dp[maxIndex]
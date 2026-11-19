class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        dp = {}
        
        def dfs(i, summ):

            if (i, summ) in dp:
                return dp[(i, summ)]

            if i == len(nums):
                if summ == target:
                    dp[(i, summ)] = 1
                    return dp[(i, summ)]
                else:
                    dp[(i, summ)] = 0
                    return dp[(i, summ)]

            
            neg = dfs(i+1, summ-nums[i])
            pos = dfs(i+1, summ+nums[i])

            dp[(i, summ)] = neg + pos

            return neg + pos
        
        return dfs(0, 0)
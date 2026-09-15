class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}
        def dfs(i, currSum):

            if i == len(nums) and currSum == target:
                return 1
            
            if i == len(nums) and currSum != target:
                return 0

            if (i, currSum) in dp:
                return dp[(i, currSum)]
            
            first_option = dfs(i+1, nums[i] + currSum)
            second_option = dfs(i+1, -nums[i] + currSum)

            dp[(i, currSum)] = first_option + second_option

            return dp[(i, currSum)]
        
        return dfs(0, 0)
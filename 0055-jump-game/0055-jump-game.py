from functools import cache
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        finalPos = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):

            if i + nums[i] >= finalPos:
                finalPos = i
            
        return finalPos == 0




        #Top down memoized soln 
        # n = len(nums)

        # @cache
        # def dfs(i):

        #     if i >= n:
        #         return False
            
        #     if i == n-1:
        #         return True
            
        #     for j in range(1, nums[i] + 1):

        #         if (dfs(i+j)):
        #             return True
            
        #     return False
        
        return dfs(0)
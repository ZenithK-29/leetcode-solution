class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        totalJumps = 0
        lastJumpIdx = 0
        coverage = 0
        destination = n-1

        for i in range(n-1):

            coverage = max(coverage, nums[i] + i)

            if i == lastJumpIdx:
                lastJumpIdx = coverage
                totalJumps+=1


                if coverage >= destination:
                    return totalJumps
        
        return totalJumps


        #TOP down memoized approach
        # @cache
        # def dfs(i):

        #     if i >= n-1:
        #         return 0
            
        #     minJump = float("inf")
        #     for j in range(i+1, i+nums[i]+1):

        #         minJump = min(minJump, 1+dfs(j))
            
        #     return minJump
        
        # return dfs(0)
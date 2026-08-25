class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def dfs(i):

            if i >= len(nums):
                return 0
            
            house_to_rob = nums[i] + dfs(i+2)
            house_to_skip = dfs(i+1)

            return max(house_to_rob, house_to_skip)
        
        return dfs(0)

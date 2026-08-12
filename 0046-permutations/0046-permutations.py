class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(curr):

            if len(curr) == len(nums):
                res.append(curr[::])
                return
            
            for i in range(0, len(nums)):

                if nums[i] not in curr:

                    curr.append(nums[i])
                    dfs(curr)

                    curr.pop()
        
        dfs([])
        return res


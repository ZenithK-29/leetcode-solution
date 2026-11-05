class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        min_best = nums[0]
        max_best = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):

            v1 = nums[i]
            v2 = nums[i] * max_best
            v3 = nums[i] * min_best

            max_best = max(v1, v2, v3)
            min_best = min(v1, v2, v3)

            res = max(res, max_best, min_best)
        
        return res
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        prefix_sum = [1] * n
        suffix_sum = [1] * n
        res = [0] * n

        for i in range(1, n):
            prefix_sum[i] = nums[i-1] * prefix_sum[i-1]
        
        for i in range(n-2, -1, -1):
            suffix_sum[i] = nums[i+1] * suffix_sum[i+1]
        
        for i in range(n):
            res[i] = suffix_sum[i] * prefix_sum[i]
        
        return res
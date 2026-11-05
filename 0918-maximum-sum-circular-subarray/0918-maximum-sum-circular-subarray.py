class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        
        currMax, globalMax = nums[0], nums[0]
        currMin, globalMin = nums[0], nums[0]
        total = sum(nums)

        for i in range(1, len(nums)):

            currMax = max(currMax+nums[i], nums[i])
            globalMax= max(currMax, globalMax)

            currMin = min(currMin+nums[i], nums[i])
            globalMin = min(currMin, globalMin)

        if globalMax < 0:
            return globalMax
        
        return max(globalMax, total-globalMin)


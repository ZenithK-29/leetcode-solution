class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        
        l, currSum = 0, 0
        minSize = float("inf")

        for r in range(len(nums)):

            currSum += nums[r]

            while currSum >= target:

                minSize = min(r-l+1, minSize)
                currSum -= nums[l]
                l +=1
        
        return 0 if minSize == float("inf") else minSize
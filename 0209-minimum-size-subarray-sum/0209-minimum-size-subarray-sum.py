class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        
        l, currSum = 0, 0
        minSum = float("inf")

        for r in range(len(nums)):

            currSum += nums[r]

            while currSum >= target:

                currSum -= nums[l]

                minSum = min(minSum, r-l+1)

                l+=1
        
        return 0 if minSum == float("inf") else minSum
        
    
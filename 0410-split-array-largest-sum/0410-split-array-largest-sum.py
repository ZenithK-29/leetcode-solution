class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        l = max(nums)
        r = sum(nums)
        res = -1

        while l <= r:

            guess = l + (r-l)//2
            validSubarray = self.helper(nums, guess)

            if validSubarray <= k:
                r = guess - 1 
                res = guess
            
            else:
                l = guess + 1
        
        return res
    
    def helper(self, nums, guess):

        subarray = 1
        aggregate = 0

        for num in nums:

            if aggregate + num <= guess:
                aggregate += num
            
            else:
                subarray += 1
                aggregate = num
        
        return subarray
                
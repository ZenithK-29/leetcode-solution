class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if 0 not in nums:
            return
        
        l = 0

        for r in range(len(nums)):

            if nums[r] != 0:

                nums[l], nums[r] = nums[r], nums[l]
                l +=1
        
        
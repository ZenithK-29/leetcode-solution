class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        count = {}

        for i in range(len(nums)):

            count[nums[i]] = i
        
        for i in range(len(nums)):

            num = nums[i]
            compliment = target - num

            if compliment in count and count[compliment] != i:
                return [i, count[compliment]]
        
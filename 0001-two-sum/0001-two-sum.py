class Solution(object):
    def twoSum(self, nums, target):
        
        count = {}

        for i in range(len(nums)):

            el = nums[i]
            if target - el in count:
                return [i, count[target-el]]

            count[el] = i




        
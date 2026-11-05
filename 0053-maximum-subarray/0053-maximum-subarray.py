class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = nums[0]

        curr_sum = 0

        for i in range(len(nums)):

            num = nums[i]

            curr_sum += num

            max_sum = max(curr_sum, max_sum)

            if curr_sum < 0:
                curr_sum = 0

        return max_sum

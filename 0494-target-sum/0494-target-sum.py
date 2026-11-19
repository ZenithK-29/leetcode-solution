class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        dp[0][0] = 1 # if i did not take any element and i want 0 theres one way i can do that

        for i in range(len(nums)):
            for currSum, count in dp[i].items():

                dp[i+1][currSum + nums[i]] += count
                dp[i+1][currSum - nums[i]] += count

        return dp[len(nums)][target]
        
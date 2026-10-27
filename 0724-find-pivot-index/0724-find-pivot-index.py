class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        

        #optimal soln

        n = len(nums)
        left = 0
        arrSum = sum(nums)

        for i in range(n):
            right = arrSum - left - nums[i]
            
            if left == right:
                return i

            left += nums[i]

        return -1


        #suboptimal soln
        # n = len(nums)
        # prefix = [0] * n
        # suffix = [0] * n

        # for i in range(1, n):
        #     prefix[i] = prefix[i-1] + nums[i-1]
        
        # for i in range(n-2, -1, -1):
        #     suffix[i] = suffix[i+1] + nums[i+1]
        
        # for i in range(n):
        #     if prefix[i] == suffix[i]:
        #         return i
        
        # return -1
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        
        count = {0:1}
        res = 0
        prefix_sum = 0

        for i in range(len(nums)):
            num = nums[i]
            prefix_sum += num
            remainder = prefix_sum % k

            if remainder in count:
                res += count.get(remainder, 0) 
            
            count[remainder] = count.get(remainder, 0) + 1
        
        return res
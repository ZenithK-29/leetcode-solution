class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        count = {}
        zeroes = 0
        ones = 0
        res = 0

        for i in range(len(nums)):
            num = nums[i]
            
            if num == 0:
                zeroes +=1
            else:
                ones += 1
            
            diff = zeroes - ones

            if diff == 0:
                res = max(res, i+1)
            
            else:
                if diff in count:
                    res = max(res, i-count[diff])
                
                else:
                    count[diff] = i

        return res
            


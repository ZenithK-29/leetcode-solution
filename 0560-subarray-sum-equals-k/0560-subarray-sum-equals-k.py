class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        total_count = 0
        currSum = 0
        prefixSumCount = {0:1}

        for num in nums:

            currSum += num

            if currSum - k in prefixSumCount:
                total_count += prefixSumCount[currSum-k]
            
            prefixSumCount[currSum] = prefixSumCount.get(currSum, 0) + 1
        
        return total_count
            

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2==1:
            return False
        
        n = len(nums)

        dp = set()
        dp.add(0)
        target = sum(nums) / 2

        for i in range(n-1, -1, -1):

            

            newDp = set()
            for t in dp:
                if nums[i] + t == target:
                    return True
                newDp.add(nums[i] + t)
                newDp.add(t)
            dp = newDp
        
        return True if target in dp else False
        

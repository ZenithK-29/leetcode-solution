class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False
        
        n = len(nums)
        dp =set()
        dp.add(0)
        target = sum(nums) / 2

        for i in range(n-1, -1, -1):

            newDp = set()

            for num in dp:
                newDp.add(nums[i] + num)
            dp.update(newDp)
        
        return True if target in dp else False

        
        
        

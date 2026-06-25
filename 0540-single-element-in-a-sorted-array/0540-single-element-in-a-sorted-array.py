class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = l + ((r-l)//2)

            if (mid - 1<0 or nums[mid] != nums[mid-1]) and (mid+1 == len(nums) or nums[mid] != nums[mid+1]):
                return nums[mid]
            
            leftSize = mid - 1 if nums[mid] == nums[mid-1] else mid

            if leftSize % 2:
                r = mid - 1
            
            else:
                l = mid + 1
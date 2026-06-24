class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        

        def binarySearch(nums, target, leftBias):

            l , r = 0 , len(nums) - 1

            i = -1
            while l <= r:

                mid = l + ((r-l)//2)

                if nums[mid] > target:
                    r = mid - 1
                
                elif nums[mid] < target:
                    l = mid + 1

                else:
                    i = mid
                    if leftBias:
                        r = mid - 1
                    else:
                        l = mid + 1
            return i
        
        left = binarySearch(nums, target, True)
        right = binarySearch(nums, target, False)

        return [left, right]
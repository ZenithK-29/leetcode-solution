class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #2pointer approach

        l,r,i = 0, len(nums)-1, 0

        while i<=r:

            num = nums[i]
            
            if num == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l+=1
                i+=1
            
            elif num == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r-=1

            else:
                i+=1

        #Corny method
        # counts = [0, 0, 0]

        # for count in nums:
        #     counts[count] +=1
        
        # R, W, B = counts

        # nums[:R] = [0]*R
        # nums[R:R+W] = [1]*W
        # nums[R+W:] = [2]*B

    

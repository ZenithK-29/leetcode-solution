class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        #optimal approach

        i = 0
        j = len(height) - 1
        leftMax = height[i]
        rightMax = height[j]
        totalWater = 0

        while i < j:

            if leftMax < rightMax: # left wall is the limit
                totalWater += leftMax - height[i]
                i +=1
                leftMax = max(leftMax, height[i])
            
            else:
                totalWater += rightMax - height[j]
                j -=1
                rightMax = max(rightMax, height[j])
        
        return totalWater





        #sub optimal apprach  
        # n=len(height)
        # left_max = [0] * len(height)
        # right_max = [0] * len(height)

        # left_max[0] = height[0]
        # right_max[n-1] = height[n-1]

        # for i in range(1, n):
        #     left_max[i] = max(left_max[i-1], height[i])
        
        # for j in range(n-2, -1, -1):
        #     right_max[j] = max(right_max[j+1], height[j])
        
        # total_water = 0

        # for k in range(n):
        #     total_water += min(left_max[k], right_max[k]) - height[k]
        
        # return total_water
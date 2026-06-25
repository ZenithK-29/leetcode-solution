class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        i = 0

        while i < len(arr) - 1 and arr[i] < arr[i+1]:

            i+=1
        
        return i
import heapq

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
        heap = []

        for ele in arr:
            heapq.heappush(heap, (-abs(x-ele), -ele))

        while len(heap) > k:
            heapq.heappop(heap)

        ans = []
        while heap:
            ans.append(-heapq.heappop(heap)[1])
        
        ans.sort()

        return ans
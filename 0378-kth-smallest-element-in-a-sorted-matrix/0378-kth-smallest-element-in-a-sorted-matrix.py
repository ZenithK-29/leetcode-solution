import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        
        
        
        heap = []
        for nums in matrix:
            for num in nums:
                heap.append(num)
        heap.sort()

        return heap[k-1]
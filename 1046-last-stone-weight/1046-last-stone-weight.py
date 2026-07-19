class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-n for n in stones]
        heapq.heapify(heap)

        while heap and len(heap) > 1:

            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)

            if stone1 - stone2 != 0:
                heapq.heappush(heap, -(stone1-stone2))
            
        return -heap[0] if len(heap) > 0 else 0
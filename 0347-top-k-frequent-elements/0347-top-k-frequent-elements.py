import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #Bucket Sort --> O(n) soln
        n = len(nums)
        bucket = [0] * (n+1)
        count = Counter(nums)

        #mapped the num to their respective indexes where the indexes matches the freq of the num
        for num, freq in count.items():

            if bucket[freq] == 0:
                bucket[freq] = [num]
            else:
                bucket[freq].append(num)
        
        res = []

        for i in range(n, -1, -1):
            if bucket[i] != 0:
                res.extend(bucket[i])
            if len(res) == k:
                break
        
        return res
        
        #heap soln
        # count = Counter(nums)
        # heap = []

        # for key, value in count.items():

        #     if len(heap) < k:
        #         heapq.heappush(heap, (value, key))
        #     else:
        #         heapq.heappushpop(heap, (value, key))
            
        # return [h[1] for h in heap]
        
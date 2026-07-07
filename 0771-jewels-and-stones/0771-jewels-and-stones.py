class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jewCount = Counter(jewels)
        count = 0

        for i in range(len(stones)):

            ch = stones[i]

            if ch in jewCount: 
                count+=1
        
        return count
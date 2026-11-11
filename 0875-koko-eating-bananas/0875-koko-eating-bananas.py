class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        res = -1
        l = 1
        r = max(piles)

        while l<=r:

            guess = l + (r-l)//2

            hour = self.time(piles, guess)

            if hour > h:
                l = guess + 1
            
            else:
                res = guess
                r = guess - 1

        return res
            
        
    
    def time(self, piles, speed):

        t = 0

        for i in range(len(piles)):

            t = t + piles[i]//speed

            if piles[i]%speed != 0:
                t +=1
        
        return t
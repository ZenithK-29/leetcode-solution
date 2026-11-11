class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:

        l = max(weights)
        r = sum(weights)
        res = -1

        while l<= r:

            guess = l + (r-l)//2

            someDays = self.noOfDays(weights, guess)

            if someDays > days:
                l = guess + 1
            
            else:
                res = guess
                r = guess - 1
            
        return res

        
    
    def noOfDays(self, weights, guess):

        day = 1
        summ = 0

        for i in range(len(weights)):

            if summ + weights[i] > guess:
                day +=1
                summ = 0
            
            summ += weights[i]
        
        return day

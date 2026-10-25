class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        
        numCopy = x
        revNum = 0

        while numCopy:

            rem = numCopy % 10
            revNum = revNum * 10 + rem
            numCopy = numCopy//10
        
        return x == revNum
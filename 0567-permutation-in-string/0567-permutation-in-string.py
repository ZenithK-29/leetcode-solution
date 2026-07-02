from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        i = 0
        j = len(s1) - 1
        countS1 = Counter(s1)

        while j < len(s2):

           
            countS2 = Counter(s2[i:j+1])

            if countS1 == countS2:
                return True
            
            i+=1
            j+=1

            if i-1 != 0 and j+1 < len(s2):
                countS2[s2[i-1]] -=1
                countS2[s2[j]] +=1
        
        return False
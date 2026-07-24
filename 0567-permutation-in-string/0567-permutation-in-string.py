class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        i = 0
        j = len(s1) - 1
        count1 = Counter(s1)
        count2 = Counter(s2[i:j+1])

        while j < len(s2):

            if count1 == count2:
                return True
            
            count2[s2[i]] -=1

            i +=1
            j +=1

            if j < len(s2):
                count2[s2[j]] +=1
        
        return False
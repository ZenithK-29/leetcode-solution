class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        i = 0
        j = len(s1) - 1
        count_s1 = Counter(s1)
        count_s2 = Counter(s2[i:j+1])

        while j < len(s2):

            if count_s1 == count_s2:
                return True
            
            count_s2[s2[i]] -=1

            i+=1
            j +=1

            if j < len(s2):
                count_s2[s2[j]] +=1
        
        return False
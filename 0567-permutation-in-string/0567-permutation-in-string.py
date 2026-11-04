class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count_1 = Counter(s1)

        count_2 = {}

        l = 0

        for r in range(len(s2)):

            count_2[s2[r]] = count_2.get(s2[r], 0) + 1

            while r-l+1 > len(s1):

                count_2[s2[l]] -=1

                if count_2[s2[l]] == 0:
                    del count_2[s2[l]]
                
                l+=1
            
            if count_1 == count_2:
                return True
        
        return False
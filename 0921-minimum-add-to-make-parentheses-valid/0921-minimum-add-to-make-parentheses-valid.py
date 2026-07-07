class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        open_para = 0
        moves = 0


        for i in range(len(s)):

            br = s[i]

            if br == "(":
                open_para +=1
            
            else:
                
                if open_para > 0:
                    open_para -=1
                else:
                    moves +=1

        return open_para + moves


       
            
            
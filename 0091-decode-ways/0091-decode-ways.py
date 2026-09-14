class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def dfs(i):

            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0
            
            optionA = dfs(i+1)

            optionB = 0

            if i + 2 <= len(s) and int(s[i:i+2]) in range(10, 27):
                optionB = dfs(i+2)
            
            return (optionA + optionB)
        
        return dfs(0)
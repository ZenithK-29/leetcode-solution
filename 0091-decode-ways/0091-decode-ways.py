class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == "0":
            return 0

        dp = [0] * (len(s)+1)

        dp[0] = 1
        dp[1] = 0 if s[0] == 0 else 1

        for i in range(2, len(s) + 1):

            if int(s[i-1:i]) in range(1, 10):
                dp[i] += dp[i-1]
            
            if int(s[i-2:i]) in range(10, 27):
                dp[i] += dp[i-2]
        
        return dp[len(s)]



        #recursive
        # @cache
        # def dfs(i):

        #     if i == len(s):
        #         return 1
            
        #     if s[i] == "0":
        #         return 0
            
        #     optionA = dfs(i+1)

        #     optionB = 0

        #     if i + 2 <= len(s) and int(s[i:i+2]) in range(10, 27):
        #         optionB = dfs(i+2)
            
        #     return (optionA + optionB)
        
        # return dfs(0)
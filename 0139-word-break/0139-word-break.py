class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        maxLen = 0
        n = len(s)
        
        for word in wordDict:
            currLen = len(word)
            maxLen = max(currLen, maxLen)
        
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):

            for j in range(i-1, max(-1, i-maxLen-1), -1):

                if dp[j] and s[j:i] in wordDict:

                    dp[i] = True
                    break
        
        return dp[n]
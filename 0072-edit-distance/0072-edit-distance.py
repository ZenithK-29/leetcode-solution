class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #word1 -> word2
        row, col = len(word2) + 1, len(word1) + 1

        dp = [[0] * col for _ in range(row)]

        dp[0][0] = 0

        for i in range(1, row):
            dp[i][0] = i
        
        for j in range(1, col):
            dp[0][j] = j
        
        for i in range(1, row):
            for j in range(1, col):

                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        return dp[row-1][col-1]
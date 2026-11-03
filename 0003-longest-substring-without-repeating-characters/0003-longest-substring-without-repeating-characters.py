class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxLen = float("-inf")
        l = 0

        count = {}

        for r in range(len(s)):

            count[s[r]] = count.get(s[r], 0) + 1

            while count[s[r]] > 1:

                count[s[l]] -=1
                l += 1
            
            maxLen = max(maxLen, r-l+1)
        
        return 0 if maxLen==float("-inf") else maxLen
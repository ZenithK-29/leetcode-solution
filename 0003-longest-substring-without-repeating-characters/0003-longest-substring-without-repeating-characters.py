class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        l = 0
        seen = {}
        maxLength = 0

        for r in range(len(s)):

            right = s[r]
            if right in seen:
                if seen[right] >= l:
                    l = seen[right] + 1
            
            seen[right] = r
            maxLength = max(maxLength, r-l+1)
        
        return maxLength
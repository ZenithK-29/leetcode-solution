class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        text = "".join(c for c in s if c.isalnum()).lower()

        i, j = 0, len(text) - 1

        while i < j:

            if text[i] != text[j]:
                return False

            i+=1
            j-=1
        
        return True

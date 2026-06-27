class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        i = 0
        j = len(needle) - 1

        while j < len(haystack):

            substr = haystack[i:j+1]

            if substr == needle:
                return i
            
            else:
                i +=1
                j+=1
        
        return -1
        
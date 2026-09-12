class Solution:
    def countSubstrings(self, s: str) -> int:
        
        totalCount = 0

        def count_all_palindrome(s, left, right):
            
            count = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:

                count +=1
                left -=1
                right+=1
            
            return count
        


        for i in range(len(s)):

            totalCount += count_all_palindrome(s, i, i)

            totalCount += count_all_palindrome(s, i, i+1)

        return totalCount

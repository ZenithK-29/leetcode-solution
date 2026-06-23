# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        l, r = 0, n
        res = 0

        while l <= r:

            mid = l + ((r-l)//2)

            if isBadVersion(mid):
                res = mid
                r = mid - 1
            
            else:
                l = mid + 1

        return l



            
        
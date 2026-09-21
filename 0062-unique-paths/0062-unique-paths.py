class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        cache = {}

        def dfs(row, col):

            if row == m-1 and col == n-1:
                return 1
            
            if (row, col) in cache:
                return cache[(row, col)]
            
            down = 0
            right = 0

            if row >= 0 and row +1 < m:
                down = dfs(row+1, col)
            
            if col >= 0 and col+1 < n:
                right = dfs(row, col+1)
            
            cache[(row, col)] = down + right

            return cache[(row, col)]

        return dfs(0, 0)

        